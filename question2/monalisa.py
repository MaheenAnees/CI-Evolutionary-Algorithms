from PIL import ImageFilter
from PIL import ImageDraw
from PIL import Image
import sys
import math
import json
import copy
import numpy as np
import random
from geneticAlgo import *
from multiprocessing import Pool

COLOUR_BLACK = (0, 0, 0, 255)
COLOUR_WHITE = (255, 255, 255, 255)
OFFSET = 10
POLYGONS = 50
POLY_MIN_POINTS = 3
POLY_MAX_POINTS = 5
IMG_SIZE = (256,256)
IMG_PATH ="./mona.bmp"


def randomPoint(width, height):
    x = random.randrange(0 - OFFSET, width + OFFSET, 1)
    y = random.randrange(0 - OFFSET, height + OFFSET, 1)
    return (x, y)


def randomColor():
    red = random.randrange(0, 256)
    green = random.randrange(0, 256)
    blue = random.randrange(0, 256)
    alpha = random.randrange(0, 256)
    return (red, green, blue, alpha)


def randomChromosome(chromosomeSize=POLYGONS, fixed_colour=False):
    shapes = []
    (width, height) = IMG_SIZE

    for i in range(POLYGONS):
        pointNo = random.randrange(POLY_MIN_POINTS, POLY_MAX_POINTS + 1)
        points = []
        for j in range(pointNo):
            point = randomPoint(width, height)
            points.append(point)
        colour = COLOUR_WHITE if fixed_colour else randomColor()
        shape = [points, colour]
        shapes.append(shape)
    return shapes


def loadImage(path):
    img = Image.open(path)
    return img

def draw(shapes, background=COLOUR_BLACK, show=False, save=False,
             generation=None):
        size = IMG_SIZE
        img = Image.new('RGB', size, background)
        draw = Image.new('RGBA', size)
        pdraw = ImageDraw.Draw(draw)
        for shape in shapes:
            colour = shape[1]
            points = shape[0]
            pdraw.polygon(points, fill=colour, outline=colour)
            img.paste(draw, mask=draw)

        if show:
            img.show()

        if save:
            fileName = u"{}".format(generation)
            saveLoc = u"{}.png".format(fileName)
            img = img.filter(ImageFilter.GaussianBlur(radius=3))
            img.save(saveLoc)
            print("saving image to {}".format(saveLoc))

        return img


class MonaLisa(GA):
    def __init__(self, totalGenerations=5000, mutationRate_=0.8, iterations_=5,  size=10, imgPath="./mona.bmp"):
        self.polygons = POLYGONS
        self.polyMin = POLY_MIN_POINTS
        self.polyMax = POLY_MAX_POINTS
        self.offset = OFFSET
        self.population = []
        self.populationSize = size
        self.totalGenerations = totalGenerations
        self.mutationRate = mutationRate_
        self.iterations = iterations_
        self.imgSize = IMG_SIZE
        self.img = loadImage(imgPath)
        self.inputImgArr = np.frombuffer(self.img.tobytes(), dtype=np.uint8).reshape((self.img.size[1], self.img.size[0], 3)) / 255

        for _ in range(self.populationSize):
            self.population.append(randomChromosome(self.imgSize))

    def calcFitness(self, image):
        image = draw(image)
        imgArr = np.frombuffer(image.tobytes(), dtype=np.uint8)
        imgArr = imgArr.reshape((self.img.size[1], self.img.size[0], 3)) / 255
        diff = np.absolute(self.inputImgArr - imgArr)
        diff = np.sum(diff, axis=(0, 1))
        fitness = math.sqrt((diff[0]*diff[0]) +
                            (diff[1]*diff[1])+(diff[2]*diff[2]))
        return 1/fitness

    def mutate(self, chromosome):
        randChr = random.randrange(0, len(chromosome))
        points = chromosome[randChr][0]
        colour = chromosome[randChr][1]
        rand = random.uniform(0, self.mutationRate)
        if rand <= self.mutationRate/2:
            idx = random.randrange(0, 4)
            value = random.randrange(0, 256)
            colour = list(colour)
            colour[idx] = value
            colour = tuple(colour)
        else:
            idx = random.randrange(0, len(points))
            point = randomPoint(IMG_SIZE[0], IMG_SIZE[1])
            points[idx] = point
        return chromosome

    def newGeneration(self):
        offsprings = []
        mutatedPop = []
        randomParent = random.randrange(0, len(self.population))
        parent = self.population[randomParent]
        child = self.mutate(parent)
        while self.calcFitness(parent) < self.calcFitness(child):
            child = self.mutate(parent)    
        parents = [parent, child]
        for i in range(self.iterations):
            offspring = self.crossOver(parents)
            offsprings.append(offspring)
        # for i in offsprings:
        #     mutatedOff = self.mutate(i)
        #     mutatedPop.append(mutatedOff)
        # self.population += mutatedPop
        survivors = self.selection('truncate', self.populationSize)
        draw(survivors[0], save=True)
        return survivors
