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

POPULATION_SIZE = 35
file = open("test.txt" , "a")
file2 = open("test1.txt" , "w")
ID='9wAwMbeZDb2T9n57mknTNdOYGuNbbe7PrPx3R7lvdilAjZzxcs'
THRESHOLD=1500000

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
                if prob < 0.125:
                    # if gp1 < -8.8:
                    #     gene = random.uniform(-10.0,gp1+1.2)
                    # elif gp1 > 8.8:
                    #     gene = random.uniform(gp1-1.2,10.0)
                    # else:
                    #     gene = random.uniform(gp1-1.2,gp1+1.2)
                    # if prob < 0.066:
                    random_float=random.uniform(i+1,i+6)
                    gene=gp1+(random.uniform(-1,1))/(10**random_float)
                    # else:
                    #     random_float=random.uniform(5,15)
                    #     gene=gp1+(random.uniform(-1,1))/(10**random_float)
                    # if i <3 :
                    #     if prob<0.5:
                    #         gene=random.uniform(-10.0,10.0)
                    #     else:
                    #         gene=gp1+random.random(-1,1)
                    gp1=gene
                child_chromosome.append(gp1)
            else:
                if prob < 0.625:
                    # if gp2 < -8.8:
                    #     gene = random.uniform(-10.0,gp2+1.2)
                    # elif gp2 > 8.8:
                    #     gene = random.uniform(gp2-1.2,10.0)
                    # else:
                    #     gene = random.uniform(gp2-1.2,gp2+1.2)
                    # if prob < 0.666:
                    random_float=random.uniform(i+1,i+6)
                    gene=gp2+(random.uniform(-1,1))/(10**random_float)
                    # else:
                    #     random_float=random.uniform(5,15)
                    #     gene=gp2+(random.uniform(-1,1))/(10**random_float)
                    # if i <3 :
                    #     if prob<5.5:
                    #         gene=random.uniform(-10.0,10.0)
                    #     else:
                    #         gene=gp2+random.random(-1,1)
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
        return fitness

def cal_min(a,b):
    if a<b:
        return a
    return b

def create_gnome():
    global TARGET_LENGTH
    gnome = [[-7.836019304743436, 1.721828521475464, -5.994260003978321, 0.04933903146360126, 0.038108481576750876, 8.132366667945717e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484611713424432e-08, 4.036350412020522e-11, -6.704733356106608e-12] ,[-7.836019304743436, 1.9804091656220617, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366667945717e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484611713424432e-08, 4.036350412020522e-11, -6.704733356106608e-12] ,[-9.544012697959436, 1.1885813106949588, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366667945717e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484611713424432e-08, 4.036350412020522e-11, -6.704733356106608e-12] ,[-9.544012697959436, 1.1885813106949588, -5.994260003978321, 0.04933903146367728, 0.038108481576750876, 8.132366667945717e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484611713424432e-08, 4.036350412020522e-11, -6.704733356106608e-12] ,[-9.544012697959436, 1.1885813106949588, -5.994260003978321, 0.04933903146360126, 0.038108481576750876, 8.132366667945717e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484611713424432e-08, 4.036350412020522e-11, -6.704733356106608e-12] ,[-9.544012697959436, 1.1885813106949588, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366667945717e-05, -6.018768797865638e-05, -1.251549100085057e-07, 3.484611713424432e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-9.544012697959436, 1.1885813106949588, -5.994260003978321, 0.04933903146367728, 0.038108481576750876, 8.132366667945717e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484611713424432e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-9.544012697959436, 1.1885813106949588, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366667945717e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484611713424432e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-9.544012697959436, 1.1885813106949588, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366678443838e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484611713424432e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-9.544012697959436, 1.1885813106949588, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366682405852e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484611713424432e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-9.257724399897878, 1.1885813106949588, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366667945717e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484611713424432e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-8.950000476918587, 1.1885813106949588, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366678443838e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.4846148674339024e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-9.128271655364124, 1.1885813106949588, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366667945717e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484611713424432e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-9.544012697959436, 1.1885813106949588, -5.994260003978423, 0.04933903146367728, 0.038108481576750876, 8.132366660970913e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484606576318202e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-9.544012697959436, 1.1885813106949588, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366667945717e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484606576318202e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-9.544012697959436, 1.6331278923663266, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366667945717e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484611713424432e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-8.950000476918587, 1.1885813106949588, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366664350214e-05, -6.018768797865638e-05, -1.251549100085057e-07, 3.484606576318202e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-8.950000476918587, 1.1885813106949588, -5.994260003978423, 0.04933903146367728, 0.038108481576750876, 8.132366667945717e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484606576318202e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-8.950000476918587, 1.1885813106949588, -5.994260003978423, 0.04933903146367728, 0.038108481576750876, 8.132366678443838e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484606576318202e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-8.950000476918587, 1.1885813106949588, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366678443838e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484606576318202e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-8.950000476918587, 1.1885813106949588, -5.9942600039784795, 0.04933903146367728, 0.038108481576750876, 8.132366678443838e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484606576318202e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-8.950000476918587, 1.1885813106949588, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366682405852e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484606576318202e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-7.682703441865617, 1.1885813106949588, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366667945717e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.4846153950303964e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-7.682703441865617, 1.1885813106949588, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366678443838e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.4846153950303964e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-7.682703441865617, 1.1885813106949588, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366682405852e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.4846153950303964e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-7.682703441865617, 1.1885813106949588, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366684905482e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.4846153950303964e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-7.440732468304468, 1.1885813106949588, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366667945717e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.4846148674339024e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-7.682703441865617, 1.1885813106949588, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366682405852e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484606576318202e-08, 4.038447256077998e-11, -6.704733356106608e-12] ,[-9.544012697959436, 1.1885813106949588, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366667945717e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484611713424432e-08, 4.038695802102256e-11, -6.704733356106608e-12] ,[-6.582286044798396, 1.1885813106949588, -5.994260003978408, 0.04933903146367728, 0.038108481576750876, 8.132366667945717e-05, -6.018768799848978e-05, -1.251549100085057e-07, 3.484611713424432e-08, 4.038447256077998e-11, -6.704733356106608e-12]]
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
    initial_models=[[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04933998825164186, 0.03811153377282071, 8.184927693167141e-05, -6.0186534576146766e-05, -1.2511953794978825e-07, 3.484634157817437e-08, 3.9875462944727475e-11, -6.7051594661433434e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04934015357991803, 0.03811153277380611, 8.184887930741602e-05, -6.0186534576146766e-05, -1.2511953794978825e-07, 3.484634278927291e-08, 3.9875462944727475e-11, -6.7051594661433434e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04934015357991803, 0.03811153277380611, 8.184887930741602e-05, -6.0186534576146766e-05, -1.2511953794978825e-07, 3.484634157817437e-08, 3.9875462944727475e-11, -6.7051594661433434e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04933998825164187, 0.038111532781909215, 8.184887637477736e-05, -6.018680330927349e-05, -1.2511953794978825e-07, 3.484630427203962e-08, 3.9876716209958466e-11, -6.7051594661433434e-12] ,[-7.751172684845402, 9.839694653658285, -6.233413161021529, 0.04933998825140147, 0.038111532781909215, 8.184887637501388e-05, -6.0186534576146766e-05, -1.2511953794978825e-07, 3.4846304271113817e-08, 3.9875462944727475e-11, -6.7051594661433434e-12] ,[-7.751172684845402, 9.839694653658285, -6.233413161021529, 0.04933998825164186, 0.03811153277380611, 8.184887637501388e-05, -6.0186534576146766e-05, -1.2511953794978825e-07, 3.484630427203962e-08, 3.9875462944727475e-11, -6.7051594661433434e-12] ,[-8.487385333709499, 9.839694653658285, -6.233413161021529, 0.04933886756795743, 0.03811153277380611, 8.184927693167072e-05, -6.018680330927064e-05, -1.2511953794978825e-07, 3.484630427202602e-08, 3.9875462944727475e-11, -6.704198621628924e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04934010814512844, 0.0381115327738061, 8.184887637477735e-05, -6.018653466057981e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.9876716209958466e-11, -6.70453766431666e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04934015346031725, 0.03811153277380611, 8.184887930741602e-05, -6.018680330927064e-05, -1.2516663061184811e-07, 3.484630427203112e-08, 3.9875462944727475e-11, -6.704547097431882e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04934015357991803, 0.0381115327819092, 8.184887930741602e-05, -6.018680330927064e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.9875462944727475e-11, -6.70454435602959e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04934015357991803, 0.038111532781909215, 8.184887637477736e-05, -6.018680330927064e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.9875462944727475e-11, -6.70454435602959e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04933998825164187, 0.038111532781909215, 8.184887637477736e-05, -6.018680330927064e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.9876716209958466e-11, -6.704544380555318e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04933998825164187, 0.038111532781909215, 8.184887637477736e-05, -6.018680330927064e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.9876716209958466e-11, -6.70454435602959e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04933998825164187, 0.038110558507788016, 8.184887930209086e-05, -6.018680330927064e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.987415359362782e-11, -6.70454435602959e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04933998824603806, 0.038110558507788016, 8.184887930209086e-05, -6.018680330927064e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.987415359362782e-11, -6.70454435602959e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04933998825164187, 0.038110558507788016, 8.184887930209086e-05, -6.018680330927064e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.9876716209958466e-11, -6.70454435602959e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04933998825102823, 0.038110558507788016, 8.184887930209086e-05, -6.018680330927064e-05, -1.2516663061183874e-07, 3.484630427202955e-08, 3.9876716209958466e-11, -6.70454435602959e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04933998825164187, 0.038110558507788016, 8.184887930191888e-05, -6.018680330927064e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.987671738644621e-11, -6.70454435602959e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04933998825164187, 0.038110558507788016, 8.184887637477735e-05, -6.0186803211128545e-05, -1.2516663061184811e-07, 3.484630427336051e-08, 3.9876716209958466e-11, -6.70454435602959e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04933998825164187, 0.038110558507788016, 8.184887637477735e-05, -6.018680330927064e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.9876716209958466e-11, -6.70454435602959e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04933998825102825, 0.0381105585077873, 8.184887930209086e-05, -6.018653525636974e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.987546330145587e-11, -6.705036834416294e-12] ,[-8.487385333709499, 9.839694653658285, -6.233413161021529, 0.04933998825102825, 0.03811164996589246, 8.184927693167141e-05, -6.018653457615017e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.987546330145587e-11, -6.70454435602959e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04933998825164187, 0.03810903430455946, 8.184887637477735e-05, -6.0186803211128545e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.9876716209958466e-11, -6.70454435602959e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04933998825164187, 0.03810903430455946, 8.184887637477735e-05, -6.018680330927064e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.9876716209958466e-11, -6.70454435602959e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04933999358376776, 0.038109024771381984, 8.184887637477735e-05, -6.0186803211128545e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.9876716209958466e-11, -6.70454435602959e-12] ,[-8.487385333709499, 9.839694653658285, -6.233413161021529, 0.049339988251028546, 0.03811153277380611, 8.184927693168526e-05, -6.018653457615017e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.987546330145587e-11, -6.70454435602959e-12] ,[-9.814759095392704, 9.839694653658285, -6.233413161021529, 0.04933998825164187, 0.03810903430455946, 8.184830042387292e-05, -6.018680330927064e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.9876716209958466e-11, -6.70453766431666e-12] ,[-8.487385333709499, 9.839694653658285, -6.233413161021529, 0.04933998825102825, 0.03811153277380611, 8.184887637477736e-05, -6.018678314031957e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.987546330145587e-11, -6.70454435602959e-12] ,[-8.487385333709499, 9.839694653658285, -6.233413161021529, 0.04933998825164186, 0.0381115327738061, 8.184887637477736e-05, -6.018680330927064e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.9876715931393304e-11, -6.70454435602959e-12] ,[-5.648816536557744, 9.839694653658285, -6.233413161021529, 0.04934015357991803, 0.038110558507788016, 8.184887930741602e-05, -6.0186534576146766e-05, -1.25119537949726e-07, 3.484634278927291e-08, 3.9876716188874776e-11, -6.705159471120935e-12] ,[-8.487385333709499, 9.839694653658285, -6.233413161021529, 0.04933998825164187, 0.03811153377282071, 8.184927693167141e-05, -6.018680330927064e-05, -1.2516663061184811e-07, 3.484630427202602e-08, 3.987546330145587e-11, -6.704198621628924e-12] ,[-6.819034658763101, 9.839694653658285, -6.233413161021529, 0.04933998825164187, 0.03810903430455946, 8.184887930209086e-05, -6.018680330927064e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.9875462944727475e-11, -6.704544380555318e-12] ,[-4.161379876619473, 9.839694653658285, -6.233413161021529, 0.04934015357991803, 0.03811153278190914, 8.184887637477736e-05, -6.018680330927064e-05, -1.2516663061184811e-07, 3.484630427202955e-08, 3.9876716209958466e-11, -6.70454435602959e-12] ,[-3.359321518544503, 9.839694653658285, -6.233413161021529, 0.04934015357991803, 0.03811153277380611, 8.184887930209086e-05, -6.018680330927064e-05, -1.2516663061184811e-07, 3.4846304272024576e-08, 3.9876716209958466e-11, -6.704547097431882e-12] ,[-3.359321518544503, 9.839694653658285, -6.233413161021529, 0.04934015357991803, 0.03811153277380611, 8.184887637477736e-05, -6.018680330927064e-05, -1.2516663061184811e-07, 3.4846304272024576e-08, 3.9875462944727475e-11, -6.7051594661433434e-12]]
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
        for _ in range(int((90*POPULATION_SIZE)/100)): 
            # parents = random.choices(population[:int((50*POPULATION_SIZE)/100)],weights=probablity_array,cum_weights=None,k=2)
            parents=[]
            parents.append(random.choice(population[:int((50*POPULATION_SIZE)/100)]))
            parents.append(random.choice(population[:int((50*POPULATION_SIZE)/100)]))
            child = parents[0].mate(parents[1])
            child_population.append(Individual(child))

        for i in range((POPULATION_SIZE-int((90*POPULATION_SIZE)/100))):
            child_population.append(population[i])
        for i in range(int((20*POPULATION_SIZE)/100)):
            print(str(i)+str(len(child_population))+str(len(population))+submit(ID,population[i].chromosome))

        population = child_population
        # temp=temp-1
        generation=generation+1
        print(generation,end=' ')
        # print(probablity_array)

if __name__ == '__main__': 
    main()