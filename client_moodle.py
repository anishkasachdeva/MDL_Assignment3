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

POPULATION_SIZE = 15
file = open("test.txt" , "a")
file2 = open("test1.txt" , "w")
# ID='9wAwMbeZDb2T9n57mknTNdOYGuNbbe7PrPx3R7lvdilAjZzxcs'
ID='3a1bPcaPVlB2IaaIobK7p1oDI8GTMwxcXET6VNPD3Rv5UAeaOp'
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
            prob = random.random()
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

def create_gnome():
    global TARGET_LENGTH
    gnome = [[-9.651242770016637, 9.991410698247897, -6.2344052132706915, 0.050069624853861995, 0.03812127804052231, 8.880296673273463e-05, -6.018812271315677e-05, -1.2500634896804526e-07, 3.4844174453087426e-08, 3.821378599400725e-11, -6.705276968296562e-12] ,[-9.651242770016676, 9.991410698247906, -6.234405213270682, 0.05006962485386219, 0.03812127804050963, 8.880296673575243e-05, -6.0188122721661806e-05, -1.2500634714716122e-07, 3.484423058306314e-08, 3.82136853972991e-11, -6.7053993919425675e-12] ,[-9.651242770016664, 9.991410698247908, -6.234405213270701, 0.05006962485386727, 0.03812127804050575, 8.880296673937579e-05, -6.0188122708679366e-05, -1.2500636951006142e-07, 3.484423712132975e-08, 3.8216029028106324e-11, -6.705270161957987e-12] ,[-9.651242770016655, 9.991410698247906, -6.234405213270694, 0.05006962485386281, 0.03812127804051798, 8.880296672572419e-05, -6.018812272005757e-05, -1.2500635952645356e-07, 3.4844202348763046e-08, 3.822109281218787e-11, -6.7051285774162036e-12] ,[-9.651242770016658, 9.991410698247899, -6.23440521327072, 0.050069624853853564, 0.03812127804050596, 8.880296674056479e-05, -6.018812270999181e-05, -1.2500637809996108e-07, 3.484422588206574e-08, 3.822109281218787e-11, -6.704935918302778e-12] ,[-9.651242770016651, 9.991410698247899, -6.2344052132706915, 0.050069624853861315, 0.038121278040530185, 8.880296673955848e-05, -6.018812270459165e-05, -1.2500635656028047e-07, 3.4844200979546654e-08, 3.822238122706639e-11, -6.705145213285573e-12] ,[-9.651242770016651, 9.991410698247904, -6.234405213270694, 0.05006962485385592, 0.0381212780405222, 8.880296672813446e-05, -6.01881227099657e-05, -1.2500635657695831e-07, 3.48442196253453e-08, 3.8218574134033615e-11, -6.705409781105211e-12] ,[-9.65124277001666, 9.991410698247893, -6.2344052132706915, 0.050069624853863355, 0.03812127804052066, 8.880296673821939e-05, -6.0188122695397286e-05, -1.2500635656028047e-07, 3.4844196540438315e-08, 3.822238122706639e-11, -6.704943006052734e-12] ,[-9.651242770016639, 9.99141069824791, -6.2344052132706915, 0.0500696248538709, 0.03812127804051046, 8.880296672105461e-05, -6.018812270850657e-05, -1.2500634077720944e-07, 3.4844174453087426e-08, 3.822238122706639e-11, -6.7047362173765256e-12] ,[-9.651242770016648, 9.991410698247902, -6.2344052132706915, 0.050069624853866984, 0.03812127804052149, 8.88029667493805e-05, -6.018812270950316e-05, -1.2500634863297075e-07, 3.4844200979546654e-08, 3.822238122706639e-11, -6.7054665799878245e-12] ,[-9.651242770016651, 9.991410698247902, -6.234405213270692, 0.05006962485385769, 0.038121278040520734, 8.880296673272594e-05, -6.018812270950316e-05, -1.250063412109319e-07, 3.484419914227699e-08, 3.822835867556516e-11, -6.7047862570043195e-12] ,[-9.651242770016637, 9.991410698247899, -6.234405213270701, 0.05006962485386596, 0.03812127804052667, 8.880296673462158e-05, -6.0188122702547396e-05, -1.250063498837095e-07, 3.4844196540438315e-08, 3.822238122706639e-11, -6.704643950689519e-12] ,[-9.651242770016658, 9.991410698247902, -6.234405213270688, 0.05006962485387111, 0.03812127804051282, 8.880296673836365e-05, -6.018812271533021e-05, -1.250063679418406e-07, 3.484421964169201e-08, 3.821032548840697e-11, -6.705883516493673e-12] ,[-9.651242770016658, 9.991410698247902, -6.234405213270687, 0.05006962485386235, 0.03812127804050818, 8.88029667273619e-05, -6.018812271533021e-05, -1.250063585850477e-07, 3.484422841828274e-08, 3.82108683770419e-11, -6.705883516493673e-12] ,[-9.651242770016676, 9.991410698247902, -6.234405213270693, 0.050069624853873985, 0.03812127804050963, 8.880296673937579e-05, -6.018812271356372e-05, -1.2500636931482011e-07, 3.484425829598848e-08, 3.821146629614063e-11, -6.705883516493673e-12]]
    gene = random.uniform(0.0,1.0)
    for i in range (len(gnome)):
        gnome[i]=gnome[i]+(gene*(1e-10))
        
    return gnome

# Driver code
def main():
    # print("la")
    global file

    global POPULATION_SIZE
    # first_individual=[0.0, 0.1240317450077846, -6.211941063144333, 0.04933903144709126, 0.03810848157715883, 8.132366097133624e-05, -6.018769160916912e-05, -1.251585565299179e-07, 3.484096383229681e-08, 4.1614924993407104e-11, -6.732420176902565e-12]
    population = []
    initial_models=[[-9.651242770016658, 9.991410698247904, -6.234405213270705, 0.05006962485388381, 0.03812127804053553, 8.880296673818939e-05, -6.018812271168578e-05, -1.2500631723853317e-07, 3.484415758072284e-08, 3.822238122706639e-11, -6.705997233708065e-12] ,[-9.651242770016665, 9.991410698247904, -6.234405213270715, 0.05006962485386944, 0.03812127804053352, 8.880296673075177e-05, -6.018812271022917e-05, -1.250063193286585e-07, 3.4844171811951585e-08, 3.822238122706639e-11, -6.705997233708065e-12] ,[-9.65124277001665, 9.991410698247904, -6.234405213270707, 0.05006962485388557, 0.03812127804053553, 8.88029667339972e-05, -6.018812271022917e-05, -1.2500632529996863e-07, 3.484415739918532e-08, 3.822238122706639e-11, -6.705997233708065e-12] ,[-9.65124277001665, 9.991410698247899, -6.234405213270707, 0.05006962485385466, 0.03812127804053553, 8.880296673442028e-05, -6.0188122709639874e-05, -1.250063238503585e-07, 3.484416519856648e-08, 3.822238122706639e-11, -6.705997233708065e-12] ,[-9.65124277001665, 9.991410698247902, -6.234405213270707, 0.05006962485385949, 0.03812127804053553, 8.880296673095491e-05, -6.018812271605511e-05, -1.25006324416076e-07, 3.484416519856648e-08, 3.822238122706639e-11, -6.705997233708065e-12] ,[-9.651242770016662, 9.991410698247904, -6.234405213270707, 0.050069624853878884, 0.038121278040525286, 8.880296672684963e-05, -6.018812271022917e-05, -1.2500632529996863e-07, 3.4844164444358815e-08, 3.822238122706639e-11, -6.705997233708065e-12] ,[-9.65124277001665, 9.991410698247902, -6.234405213270707, 0.050069624853856354, 0.03812127804053553, 8.880296673095491e-05, -6.0188122707768995e-05, -1.2500632529996863e-07, 3.484416480054842e-08, 3.822238122706639e-11, -6.705997233708065e-12] ,[-9.651242770016662, 9.991410698247902, -6.234405213270707, 0.05006962485388381, 0.03812127804053553, 8.880296672684963e-05, -6.018812271022917e-05, -1.2500632529996863e-07, 3.484416480054842e-08, 3.822238122706639e-11, -6.705997233708065e-12] ,[-9.65124277001665, 9.991410698247904, -6.234405213270707, 0.05006962485388381, 0.03812127804053358, 8.880296672355144e-05, -6.018812271022917e-05, -1.2500632529996863e-07, 3.484416480054842e-08, 3.822238122706639e-11, -6.705997233708065e-12] ,[-9.65124277001665, 9.991410698247902, -6.234405213270707, 0.05006962485385949, 0.03812127804053358, 8.880296672355144e-05, -6.018812271605511e-05, -1.2500632529996863e-07, 3.484416519856648e-08, 3.822238122706639e-11, -6.705997233708065e-12] ,[-9.65124277001665, 9.991410698247908, -6.234405213270707, 0.05006962485385949, 0.03812127804053358, 8.880296673442028e-05, -6.018812271605511e-05, -1.2500632529996863e-07, 3.484416817601826e-08, 3.822238122706639e-11, -6.705997233708065e-12] ,[-9.65124277001665, 9.991410698247904, -6.234405213270707, 0.05006962485385949, 0.03812127804053553, 8.880296673442028e-05, -6.018812271605511e-05, -1.2500632529996863e-07, 3.484417060527989e-08, 3.822238122706639e-11, -6.705997233708065e-12] ,[-9.651242770016657, 9.991410698247911, -6.234405213270707, 0.05006962485386944, 0.03812127804053352, 8.880296673095491e-05, -6.018812270755661e-05, -1.2500632910760098e-07, 3.484416480054842e-08, 3.822238122706639e-11, -6.705997233708065e-12] ,[-9.651242770016648, 9.991410698247902, -6.234405213270707, 0.05006962485386133, 0.03812127804052497, 8.880296673095491e-05, -6.0188122707768995e-05, -1.2500632910760098e-07, 3.484416519856648e-08, 3.822238122706639e-11, -6.705997233708065e-12] ,[-9.651242770016665, 9.991410698247904, -6.234405213270707, 0.05006962485388381, 0.03812127804053352, 8.880296672946088e-05, -6.0188122711536936e-05, -1.2500632529996863e-07, 3.4844147741000914e-08, 3.82229479980953e-11, -6.705997233708065e-12]]
    for i in initial_models:
        population.append(Individual(i))
    # population.append(Individual(first_individual))
    generation=0
    # while(len(population)<POPULATION_SIZE):
    #     x=create_gnome()
    #     population.append(Individual(x))
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
            # parents = random.choices(population[:int((50*POPULATION_SIZE)/100)],weights=probablity_array,cum_weights=None,k=2)
            parents=[]
            parents.append(random.choice(population[:int((50*POPULATION_SIZE)/100)]))
            parents.append(random.choice(population[:int((50*POPULATION_SIZE)/100)]))
            child = parents[0].mate(parents[1])
            child_population.append(Individual(child))

        for i in range((POPULATION_SIZE-int((80*POPULATION_SIZE)/100))):
            child_population.append(population[i])
        # for i in range(int((20*POPULATION_SIZE)/100)):
        #     print(str(i)+str(len(child_population))+str(len(population))+submit(ID,population[i].chromosome))

        population = child_population
        # temp=temp-1
        generation=generation+1
        print(generation,end=' ')
        # print(probablity_array)

if __name__ == '__main__': 
    main()