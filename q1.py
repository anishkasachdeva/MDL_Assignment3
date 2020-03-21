import json
import requests
import numpy as np
import random
import os

######### DO NOT CHANGE ANYTHING IN THIS FILE ##################
API_ENDPOINT = 'http://10.4.21.147'
PORT = 3000
MAX_DEG = 11
TARGET_LENGTH=11

POPULATION_SIZE = 10
file = open("models.txt" , "a")
ID='9wAwMbeZDb2T9n57mknTNdOYGuNbbe7PrPx3R7lvdilAjZzxcs'
THRESHOLD=1000000

#### functions that you can call
def break_condition(population):
    sum=0
    for i in population:
        sum=sum+i.fitness
    sum=sum/POPULATION_SIZE
    if sum < THRESHOLD:
        return False
    return True

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
    def _init_(self, chromosome):
        global ID
        global file
        self.chromosome = chromosome
        self.err_value = get_errors(ID,self.chromosome)
        file.write(str(self.chromosome ))
        file.write(" ")
        file.write(str(self.err_value))
        file.write("\n")
        self.fitness = self.cal_fitness()


    def mate(self, par2):
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):
            prob = random.random()
            if prob < 0.45:
                child_chromosome.append(gp1)
            elif prob < 0.90:
                child_chromosome.append(gp2)
            else:
                child_chromosome.append(random.uniform(0.0,20.0)-10)
        return Individual(child_chromosome,self.file)


    def probability(self):
        pass


    def cal_fitness(self):
        fitness = self.err_value[0] + self.err_value[1]
        return fitness

 
def create_gnome():
    global TARGET_LENGTH
    gnome = []
    gnome_len = TARGET_LENGTH
    for i in range (gnome_len):
        gene = random.uniform(0.0,20.0)
        gene=gene-10
        gnome.append(gene)
        
    return gnome

# Driver code
def main():
    # print("la")
    global file

    global POPULATION_SIZE
    #current generation
    # generation = 1
    # found = False
    ## what i have understood is that population is an array of objects
    first_individual=[0.0, 0.1240317450077846, -6.211941063144333, 0.04933903144709126, 0.03810848157715883, 8.132366097133624e-05, -6.018769160916912e-05, -1.251585565299179e-07, 3.484096383229681e-08, 4.1614924993407104e-11, -6.732420176902565e-12]
    population = []

    population.append(Individual(first_individual))

    while(len(population)<POPULATION_SIZE):
        x=create_gnome()
        population.append(Individual(x))

    while(break_condition(population)):
        child_population = []
		## for adding the individuals with least fitness score. We need to sort based on fitness score??
		# child_population.extend(population[:5]) 
		parent1 = random.choice(population[:8])
        parent2 = random.choice(population[:8])
		child = parent1.mate(parent2)
		child_population.append(Individual(child))

	population = child_population

        # index_p1,index_p2=
    ## Changed to (population_size - 1) bcz we have already added an individual
    # create initial population
    # for _ in range(POPULATION_SIZE - 1):
    #     gnome = Individual.create_gnome()
    #     err_value = get_error(file,gnome)
    #     population.append(Individual(gnome,err_value))
        
    # while not found:
    #     #sort the population in increasing order of fitness score
    #     population = sorted(population, key = lambda x:x.fitness)

    #     # if the individual having lowest fitness score ie. 
    #     # 0 then we know that we have reached to the target 
    #     # and break the loop
        
    #     if population[0].fitness <= 0:
    #         found = True
    #         break
    #     # Otherwise generate new offsprings for new generation

    #     new_generation = []
    #     # Perform Elitism, that mean 10% of fittest population
    #     # # goes to the next generation
    #     s = int((10*POPULATION_SIZE)/100)
    #     new_generation.extend(population[:s]) 

    #     # From 50% of fittest population, Individuals 
    #     # will mate to produce offspring
    #     s = int((90*POPULATION_SIZE)/100)
    #     for _ in range(s):
    #         parent1 = random.choice(population[:5])
    #         parent2 = random.choice(population[:5])
    #         child = parent1.mate(parent2)
    #         err_value = get_errors(file,child)
    #         # new_child = Individual(child,err_value)
    #         new_generation.append(Individual(child,err_value))
            
    #     population = new_generation 

    #     generation += 1

if _name_ == '_main_': 
    main()