import json
import requests
import numpy as np
import random
import os

class model(object):
    def __init__(self,model,err):
        self.model=model
        self.err=err
        self.fitness=self.cal_fitness()
    # def __eq__(self, other):
    #     return self.model==other.model
    # def __hash__(self):
    #     return hash(str(self.model))
    def cal_fitness(self):
        fitness = 2*(self.err[0] + self.err[1]) +abs(self.err[0] - self.err[1])
        return fitness

# def compare_models(model1,model2):
#     for i,j in zip(model1.model,model2.model):
#         if i!=j:
#             return False
#     return True

f = open('models.txt','r')
message = f.read()
lines=message.split('\n')
lines=lines[0:len(lines)-1]
# print(lines[len(lines)-1])
models=[]
for line in lines:
    arrays=line[1:(len(line)-2)].split('] [')
    model_numbers=[]
    err_numbers=[]
    model_string=arrays[0].split(', ')
    err_string=arrays[1].split(', ')
    for i in model_string:
        model_numbers.append(float(i))
    for i in err_string:
        err_numbers.append(float(i))
    models.append(model(model_numbers,err_numbers))
models = sorted(models, key = lambda x:x.fitness)
# models=set(models)
# models=list(models)
# print(len(models))
it=0
count=0
distinct_fitness_index=[]
while it<(len(models)-1):
    while models[it].fitness==models[it+1].fitness and it<(len(models)-1):
        it=it+1
    distinct_fitness_index.append(it)
    count=count+1
    it=it+1
if models[len(models)-2].fitness!=models[len(models)-1].fitness :
    distinct_fitness_index.append(len(models)-1)
    count=count+1
# print(count)
# print("[",end='')
for j in range(100):
    print(j+1,end=' ')
    print(distinct_fitness_index[j],end=' ')
    print(models[distinct_fitness_index[j]].err ,end=' ')
    print(models[distinct_fitness_index[j]].fitness)
    # print("[",end=' ')
    # print(distinct_fitness_index[j],end=' ')
    # print(models[distinct_fitness_index[j]].model ,end=' ')
    # print(",",end='')
    # print(models[distinct_fitness_index[j]].fitness)
    # print(models[distinct_fitness_index[j]].err)
# # print("\r",end='')
# print("]")
f.close()