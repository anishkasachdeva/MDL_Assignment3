import json
import requests
import numpy as np
import random
import os
from random import randint
######### DO NOT CHANGE ANYTHING IN THIS FILE ##################
API_ENDPOINT = 'http://10.4.21.147'
PORT = 3000
MAX_DEG = 11
TARGET_LENGTH=11

POPULATION_SIZE = 10
file = open("test.txt" , "a")
file2 = open("test1.txt" , "w")
ID='9wAwMbeZDb2T9n57mknTNdOYGuNbbe7PrPx3R7lvdilAjZzxcs'
# ID='3a1bPcaPVlB2IaaIobK7p1oDI8GTMwxcXET6VNPD3Rv5UAeaOp'
THRESHOLD=1500000
goal=500000
#### functions that you can call
# def break_condition(population):
#     sum=0
#     for i in population:
#         sum=sum+i.fitness
#     sum=sum/POPULATION_SIZE
#     if sum < THRESHOLD:
#         return False
#     return True

def get_errors(id, vector):
    """
    returns python array of length 2 
    (train error and validation error)
    """
    for i in vector: assert -10<=abs(i)<=10
    assert len(vector) == MAX_DEG

    return json.loads(send_request(id, vector, 'geterrors'))

def submit(id, vector):
    """
    used to make official submission of your weight vector
    returns string "successfully submitted" if properly submitted.
    """
    for i in vector: assert -10<=abs(i)<=10
    assert len(vector) == MAX_DEG
    return send_request(id, vector, 'submit')

#### utility functions
def urljoin(root, port, path=''):
    root = root + ':' + str(port)
    if path: root = '/'.join([root.rstrip('/'), path.rstrip('/')])
    return root

def send_request(id, vector, path):
    api = urljoin(API_ENDPOINT, PORT, path)
    vector = json.dumps(vector)
    response = requests.post(api, data={'id':id, 'vector':vector}).text
    if "reported" in response:
        print(response)
        exit()

    return response




class Individual(object):
    def __init__(self,chromosome):
        global ID
        global file
        self.chromosome = chromosome
        self.err_value = get_errors(ID,self.chromosome)
        file.write(str(self.chromosome ))
        file.write(" ")
        file.write(str(self.err_value))
        file.write("\n")
        file2.write(str(self.chromosome ))
        file2.write(" ")
        file2.write(str(self.err_value))
        file2.write("\n")
        self.fitness = self.cal_fitness()


    def mate(self, par2):
        child_chromosome = []
        i=0
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):
            prob = random.uniform(0.0,1.0)
            # if prob < 0.4:
            #     if prob < 0.0125:
            #         gene = random.uniform(-1.0,1.0)
            #         gp1=gp1+(gene*(1e-13))
            #     child_chromosome.append(gp1)
            # elif prob < 0.80:
            #     if prob < 0.4125:
            #         gene = random.uniform(-1.0,1.0)
            #         gp2=gp2+(gene*(1e-13))
            #     child_chromosome.append(gp2)
            # else:
            #     child_chromosome.append(random.uniform(0.0,20.0)-10)
            if prob < 0.5:
                if prob < 0.15:
                    # if gp1 < -8.8:
                    #     gene = random.uniform(-10.0,gp1+1.2)
                    # elif gp1 > 8.8:
                    #     gene = random.uniform(gp1-1.2,10.0)
                    # else:
                    #     gene = random.uniform(gp1-1.2,gp1+1.2)
                    # if prob < 0.066:
                    # random_float=random.uniform(i+1,i+9)
                    # gene=gp1+(randint(-9,9) + random.uniform(-0.999999999999999,0.999999999999999))/(10**random_float)
                    # if prob<0.075:
                    #     gene=gp1+random.uniform(-1.0e-14,1.0e-14)
                    # else:
                    gene=gp1*random.uniform(0.99,1.01)
                    # else:
                    #     random_float=random.uniform(5,15)
                    #     gene=gp1+(random.uniform(-1,1))/(10**random_float)
                    # if i <3 :
                    #     if prob<0.5:
                    #         gene=random.uniform(-10.0,10.0)
                    #     else:
                    #         gene=gp1+random.random(-1,1)
                    if abs(gene)<=10:
                        gp1=gene
                child_chromosome.append(gp1)
            else:
                if prob < 0.65:
                    # if gp2 < -8.8:
                    #     gene = random.uniform(-10.0,gp2+1.2)
                    # elif gp2 > 8.8:
                    #     gene = random.uniform(gp2-1.2,10.0)
                    # else:
                    #     gene = random.uniform(gp2-1.2,gp2+1.2)
                    # if prob < 0.666:
                    # random_float=random.uniform(i+1,i+9)
                    # gene=gp2+(randint(-9,9) + random.uniform(-0.999999999999999,0.999999999999999))/(10**random_float)
                    # if prob<0.075:
                    #     gene=gp2+random.uniform(-1.0e-14,1.0e-14)
                    # else:
                    gene=gp2*random.uniform(0.99,1.01)
                    # else:
                    #     random_float=random.uniform(5,15)
                    #     gene=gp2+(random.uniform(-1,1))/(10**random_float)
                    # if i <3 :
                    #     if prob<5.5:
                    #         gene=random.uniform(-10.0,10.0)
                    #     else:
                    #         gene=gp2+random.random(-1,1)
                    if abs(gene)<=10:
                        gp2=gene
                child_chromosome.append(gp2)
            # else:
            #     child_chromosome.append(random.uniform(0.0,20.0)-10)
            i=i+1
        return child_chromosome


    def probability(self):
        pass

    def cal_fitness(self):
        fitness = (self.err_value[0] + self.err_value[1])
        # fitness = (self.err_value[0]-goal)**2+(self.err_value[1]-goal)**2
        return fitness

def cal_min(a,b):
    if a<b:
        return a
    return b

def create_gnome(first_indivisual):
    global TARGET_LENGTH
    gnome=[]
    t=random.uniform(-1e-13,1e-13)
    for i in first_indivisual:
        gnome.append(i+t)
    return gnome

# Driver code
def main():
    # print("la")
    global file

    global POPULATION_SIZE
    first_individual=[-9.379350612125615, 9.990652643162875, -6.327404262054427, 0.05036354116497963, 0.03816357846950694, 9.232486133163227e-05, -6.0196348455253764e-05, -1.2511385985011592e-07, 3.484602287848356e-08, 3.751070817071005e-11, -6.705997233708065e-12]
    population = []
    # initial_models=[[-9.501956806025264, 9.990652643162875, -6.3097581782263585, 0.05024288377350588, 0.03816357846950694, 9.232486133163227e-05, -6.0196348455253764e-05, -1.2511385985011592e-07, 3.484602287848356e-08, 3.751070817071005e-11, -6.705997233708065e-12] ,[-9.57525661126483, 9.990652643162875, -6.311351457154483, 0.05024288377350588, 0.03816357846950694, 9.225201988068667e-05, -6.0196348455253764e-05, -1.2511385985011592e-07, 3.484602287848356e-08, 3.751070817071005e-11, -6.705997233708065e-12] ,[-9.501956806025264, 9.990652643162875, -6.3097581782263585, 0.05024288377350588, 0.03816357846950694, 9.225201988068667e-05, -6.0196348455253764e-05, -1.2511385985011592e-07, 3.484602287848356e-08, 3.751070817071005e-11, -6.705997233708065e-12] ,[-9.57525661126483, 9.990652643162875, -6.311351457154483, 0.05024288377350588, 0.03816357846950694, 9.225201988068667e-05, -6.0196348455253764e-05, -1.2497788853381026e-07, 3.484602287848356e-08, 3.751070817071005e-11, -6.705997233708065e-12] ,[-9.492739764056957, 9.98533994521687, -6.311351457154483, 0.05024288377350588, 0.03816357846950694, 9.225201988068667e-05, -6.0196348455253764e-05, -1.2497788853381026e-07, 3.484602287848356e-08, 3.751070817071005e-11, -6.705997233708065e-12] ,[-9.57525661126483, 9.990652643162875, -6.349213657685561, 0.05024288377350588, 0.03816357846950694, 9.225201988068667e-05, -6.0196348455253764e-05, -1.2511385985011592e-07, 3.484602287848356e-08, 3.751070817071005e-11, -6.705997233708065e-12] ,[-9.57525661126483, 9.990652643162875, -6.299079093318846, 0.05024288377350588, 0.03816357846950694, 9.225201988068667e-05, -6.0196348455253764e-05, -1.2511385985011592e-07, 3.484602287848356e-08, 3.751070817071005e-11, -6.705997233708065e-12] ,[-9.501956806025264, 9.990652643162875, -6.3097581782263585, 0.05024288377350588, 0.03816357846950694, 9.209664697788951e-05, -6.0196348455253764e-05, -1.2511385985011592e-07, 3.484602287848356e-08, 3.751070817071005e-11, -6.705997233708065e-12] ,[-9.527585204361534, 9.916155541480308, -6.326997061721416, 0.05037893138264459, 0.03816357846950694, 9.175508464989471e-05, -6.0196348455253764e-05, -1.2511385985011592e-07, 3.484602287848356e-08, 3.7603416829275524e-11, -6.705997233708065e-12] ,[-9.501956806025264, 9.990652643162875, -6.369892747744479, 0.05024288377350588, 0.03816357846950694, 9.225201988068667e-05, -6.0196348455253764e-05, -1.2497788853381026e-07, 3.484602287848356e-08, 3.751070817071005e-11, -6.705997233708065e-12]]
    # for i in initial_models:
    #     population.append(Individual(i))
    population.append(Individual(first_individual))
    generation=0
    while(len(population)<POPULATION_SIZE):
        x=create_gnome(first_individual)
        population.append(Individual(x))
    # population = sorted(population, key = lambda x:x.fitness)
    # temp=5
    # while(temp):
    while(1):
        population = sorted(population, key = lambda x:x.fitness)
        child_population = []
        ## for adding the individuals with least fitness score. We need to sort based on fitness score??
        # child_population.extend(population[:5]) 
        probablity_array=[]
        fitness_sum=0
        for i in range(int((50*POPULATION_SIZE)/100)):
            fitness_sum=fitness_sum+population[i].fitness
        for i in range(int((50*POPULATION_SIZE)/100)):
            probablity_array.append(fitness_sum/population[i].fitness)
        for _ in range(int((80*POPULATION_SIZE)/100)): 
            parents = random.choices(population[:int((50*POPULATION_SIZE)/100)],weights=probablity_array,cum_weights=None,k=2)
            # parents=[]
            # parents.append(random.choice(population[:int((50*POPULATION_SIZE)/100)]))
            # parents.append(random.choice(population[:int((50*POPULATION_SIZE)/100)]))
            child = parents[0].mate(parents[1])
            child_population.append(Individual(child))

        for i in range((POPULATION_SIZE-int((80*POPULATION_SIZE)/100))):
            child_population.append(population[i])

        print()
        print(generation)
        for i in population:
            print(i.fitness,end=' ')
        print()
        print(probablity_array)
        for i in range(int((20*POPULATION_SIZE)/100)):
            print(str(i)+str(len(child_population))+str(len(population))+submit(ID,population[i].chromosome))
        print()
        generation=generation+1
        population = child_population
        # temp=temp-1

if __name__ == '__main__': 
    main()