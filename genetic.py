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
file3=open("trace.txt","w")
ID='9wAwMbeZDb2T9n57mknTNdOYGuNbbe7PrPx3R7lvdilAjZzxcs'
file3.write('Initial Population Size: '+str(POPULATION_SIZE)+'\n')
# ID='3a1bPcaPVlB2IaaIobK7p1oDI8GTMwxcXET6VNPD3Rv5UAeaOp'
# ID='RWa9YsZpmRsTIVbq5C8ZUA5HIE2Lkfcny3R0fviRPeCEtzNrj9'
# ID='i0ZxSBn9KTktTOfG5xlLZ9CrNY2hEhg8SnLisL4CHNHGtYuqLf'
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

    # def mate2(self,par2):
    #     child_chromosome = []
    #     i=0
    #     for gp1, gp2 in zip(self.chromosome, par2.chromosome):
    #         prob = random.uniform(0.0,1.0)
    #         if i not in ([0,5,9])
    #             if prob < 0.5:
    #                 if prob < 0.15V
    #                         gene=gp1*random.uniform(0.99,1.01)
    #                         while abs(gene)>10:
    #                             gene=gp1*random.uniform(0.99,1.01))
    #                     gp1=gene
    #                 child_chromosome.append(gp1)
    #             else:
    #                 if prob < 0.65:
    #                     if prob<5.075:
    #                         gene=gp2+random.uniform(-1.0e-14,1.0e-14)
    #                         while abs(gene)>10:
    #                             gene=gp2+random.uniform(-1.0e-14,1.0e-14)
    #                     else:
    #                         gene=gp2*random.uniform(0.99,1.01)
    #                         while abs(gene)>10:
    #                             gene=gp2*random.uniform(0.99,1.01)
    #                     gp2=gene
    #             child_chromosome.append(gp2)
    #         i=i+1
    #     return child_chromosome

    def mate(self, par2):
        child_chromosome = []
        child_chromosome_without_mutation=[]
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
                child_chromosome_without_mutation.append(gp1)
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
                    # if prob<0.075:
                    #     gene=gp1+random.uniform(-1.0e-14,1.0e-14)
                    #     while abs(gene)>10:
                    #         gene=gp1+random.uniform(-1.0e-14,1.0e-14)
                    # else:
                    gene=gp1*random.uniform(0.99,1.01)
                    while abs(gene)>10:
                        gene=gp1*random.uniform(0.99,1.01)
                    # else:
                    #     random_float=random.uniform(5,15)
                    #     gene=gp1+(random.uniform(-1,1))/(10**random_float)
                    # if i <3 :
                    #     if prob<0.5:
                    #         gene=random.uniform(-10.0,10.0)
                    #     else:
                    #         gene=gp1+random.random(-1,1)
                    # while abs(gene)>10:
                    #     gene=gp1*random.uniform(0.97,1.03)
                        # gene=gp1+random.uniform(-1.0e-14,1.0e-14)
                    # if(gp1<0):
                    #     gene=random.uniform(gp1,gp1/8)
                    # else:
                    #     gene=random.uniform(gp1/8,gp1)
                    gp1=gene
                child_chromosome.append(gp1)
            else:
                child_chromosome_without_mutation.append(gp2)
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
                    # if prob<5.075:
                    #     gene=gp2+random.uniform(-1.0e-14,1.0e-14)
                    #     while abs(gene)>10:
                    #         gene=gp2+random.uniform(-1.0e-14,1.0e-14)
                    # else:
                    gene=gp2*random.uniform(0.99,1.01)
                    while abs(gene)>10:
                        gene=gp2*random.uniform(0.99,1.01)
                    # else:
                    #     random_float=random.uniform(5,15)
                    #     gene=gp2+(random.uniform(-1,1))/(10**random_float)
                    # if i <3 :
                    #     if prob<5.5:
                    #         gene=random.uniform(-10.0,10.0)
                    #     else:
                    #         gene=gp2+random.random(-1,1)
                    # while abs(gene)>10:
                    #     gene=gp2*random.uniform(0.98,1.02)
                        # gene=gp2+random.uniform(-1.0e-14,1.0e-14)
                    # if(gp2<0):
                    #     gene=random.uniform(gp2,gp2/8)
                    # else:
                    #     gene=random.uniform(gp2/8,gp2)
                    gp2=gene
                child_chromosome.append(gp2)
            # else:
            #     child_chromosome.append(random.uniform(0.0,20.0)-10)
            i=i+1
        return child_chromosome,child_chromosome_without_mutation


    def probability(self):
        pass

    def cal_fitness(self):
        fitness = (self.err_value[0] + self.err_value[1])
        # fitness = (self.err_value[0]-goal)**2+(self.err_value[1]-goal)**2
        return fitness

def create_gnome(first_indivisual):
    global TARGET_LENGTH
    gnome=[]
    for i in first_indivisual:
        t=0
        # if(i<0):
        #     t=random.uniform(i/3,0.0)
        # else:
        #     t=random.uniform(0.0,i/3)
        t=i*random.uniform(0.98,1.02)
        while abs(t)>10:
            t=i*random.uniform(0.98,1.02)
        gnome.append(t)
    return gnome

def write_init_population(population):
    file2.write('initial population \n')
    for i in range(len(population)):
        file3.write('\nIndividual '+str(i+1)+' : '+str(population[i].chromosome)+'\n'+'error'+str(population[i].err_value)+'\n'+'fitness='+str(population[i].fitness)+'\n')

def draw_line():
    file3.write('\n')
    for _ in range(100):
        file3.write('-')
    file3.write('\n')

def write_parent_child(parents,child,child_without_mutation,i):
    file3.write('\n' +'Parent 1 : '+ str(parents[0].chromosome)+'\n' +'Parent 2 : '+ str(parents[1].chromosome)+'\n'+'Child without mutation : '+str(child_without_mutation)+'\n'+'Child after mutation : '+str(child.chromosome)+'\n'+'child error : '+str(child.err_value)+'\n'+'child fitness='+str(child.fitness)+'\n')
# Driver code
def main():
    # print("la")
    global file

    global POPULATION_SIZE
    first_individual=[2.349075744862104e-13, 0.014425703629479153, -1.1361448859316574, 0.051054964516698706, 0.005061732407403513, 9.826304241788554e-06, -7.3450720289047845e-06, -1.5595696162142963e-08, 4.077322076012854e-09, 5.5076382593579015e-12, -7.655079888264856e-13]
    population = []
    # initial_models=[[-8.594284454758105, 9.516798319865098, -6.481068131922134, 0.0506405714222859, 0.037527764880970836, 9.161565240861872e-05, -5.862062663258982e-05, -1.2009423020727045e-07, 3.387952618073566e-08, 3.532919925808302e-11, -6.527022490082299e-12] ,[-8.573713357380708, 9.463989020391521, -6.478197866348896, 0.05061989627840482, 0.037527764880970836, 9.08842853386002e-05, -5.862062663258982e-05, -1.197944546901582e-07, 3.387952618073566e-08, 3.532919925808302e-11, -6.527022490082299e-12] ,[-8.573713357380708, 9.463989020391521, -6.478197866348896, 0.0506198962783972, 0.037527764880970836, 9.088428533775292e-05, -5.862062663258982e-05, -1.197944546901582e-07, 3.3879528022178014e-08, 3.532919925808302e-11, -6.527022490082299e-12] ,[-8.573713357380708, 9.46398902039153, -6.478197866348899, 0.05061989627841396, 0.03752776488096319, 9.088428532905496e-05, -5.862062662670342e-05, -1.197944546901582e-07, 3.387952811404577e-08, 3.532919925808302e-11, -6.527022490082299e-12] ,[-8.573713357380708, 9.463989020391526, -6.478197866348896, 0.05061989627841396, 0.03752776488096319, 9.088428532905496e-05, -5.862062662670342e-05, -1.197944546901582e-07, 3.387952811404577e-08, 3.532919925808302e-11, -6.527022490082299e-12] ,[-8.573713357380706, 9.463989020391521, -6.478197866348896, 0.05061989627841396, 0.037527764880970836, 9.088428532905496e-05, -5.862062662670342e-05, -1.1979446068297825e-07, 3.387952811404577e-08, 3.532919925808302e-11, -6.527022490082299e-12] ,[-8.573713357380708, 9.463989020391518, -6.478197866348881, 0.05061989627840482, 0.037527764880970836, 9.088428532025242e-05, -5.862062664253632e-05, -1.1979444461567846e-07, 3.387953100071722e-08, 3.532919925808302e-11, -6.527022490082299e-12] ,[-8.573713357380708, 9.463989020391537, -6.4781978663488955, 0.05061989627839631, 0.0375277648809663, 9.088428533577524e-05, -5.86206266358121e-05, -1.197944466104225e-07, 3.387953100071722e-08, 3.532919925808302e-11, -6.527022490082299e-12] ,[-8.573713357380708, 9.463989020391528, -6.478197866348887, 0.05061989627840482, 0.037527764880970836, 9.088428532025242e-05, -5.86206266358121e-05, -1.1979445026160566e-07, 3.387953100071722e-08, 3.532919925808302e-11, -6.527022490082299e-12] ,[-8.573713357380708, 9.463989020391528, -6.478197866348881, 0.05061989627840482, 0.03752776488096776, 9.088428532025242e-05, -5.862062662995246e-05, -1.1979445026160566e-07, 3.387953100071722e-08, 3.532919925808302e-11, -6.527022490082299e-12]]
    # for i in initial_models:
    #     population.append(Individual(i))
    population.append(Individual(first_individual))
    generation=0
    while(len(population)<POPULATION_SIZE):
        x=create_gnome(first_individual)
        population.append(Individual(x))
    write_init_population(population)
    draw_line()
    # return
    # population = sorted(population, key = lambda x:x.fitness)
    # temp=5
    # while(temp):
    count=1
    while(count<11):
        file3.write('\n' + 'Iteration ' + str(count) + '\n')
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
        for i in range(int((80*POPULATION_SIZE)/100)): 
            parents = random.choices(population[:int((50*POPULATION_SIZE)/100)],weights=probablity_array,cum_weights=None,k=2)
            # parents=[]
            # parents.append(random.choice(population[:int((50*POPULATION_SIZE)/100)]))
            # parents.append(random.choice(population[:int((50*POPULATION_SIZE)/100)]))
            child,child_without_mutation = parents[0].mate(parents[1])
            child=Individual(child)
            child_population.append(child)
            write_parent_child(parents,child,child_without_mutation,i+1)
        for i in range((POPULATION_SIZE-int((80*POPULATION_SIZE)/100))):
            file3.write('\n'+'Inherited parent '+str(i+1)+' : '+str(population[i].chromosome)+'\n')
            child_population.append(population[i])

        print()
        print(generation)
        for i in population:
            print(i.fitness,end=' ')
        print()
        print(probablity_array)
        # for i in range(int((20*POPULATION_SIZE)/100)):
        #     print(str(i)+str(len(child_population))+str(len(population))+submit(ID,population[i].chromosome))
        print()
        generation=generation+1
        population = child_population
        count=count+1
        # temp=temp-1
        draw_line()

if __name__ == '__main__': 
    main()