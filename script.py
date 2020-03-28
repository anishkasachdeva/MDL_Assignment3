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
        fitness = (self.err[0] + self.err[1])
        return fitness

# def compare_models(model1,model2):
#     for i,j in zip(model1.model,model2.model):
#         if i!=j:
#             return False
#     return True

f = open('test1.txt','r')
f2=open('test2.txt','w')
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


# ttt=0
# for i in models:
#     ttt=1
#     for j in i.model:
#         if j>10 or j< -10:
#             ttt=0
#     if i.err[0]<=10000000 and i.err[1]<=10000000 and ttt==1:
#         f2.write(str(i.model))
#         f2.write(" ")
#         f2.write(str(i.err))
#         f2.write("\n")
# f2.close()


models = sorted(models, key = lambda x:x.fitness)


# models=set(models)
# models=list(models)
# print(len(models))


it=0
count=0
distinct_fitness_index=[]
# print(len(models))
while it<(len(models)-1):
    while it<(len(models)-1) and models[it].fitness==models[it+1].fitness :
        it=it+1
    distinct_fitness_index.append(it)
    count=count+1
    it=it+1
if models[len(models)-2].fitness!=models[len(models)-1].fitness :
    distinct_fitness_index.append(len(models)-1)
    count=count+1


# print(count)
# probablity_array=[1,2,3,4]
# population=[1,2,3,4]
# fitness_sum=0
# parents = random.choices(population,weights=probablity_array,cum_weights=None,k=100)
# print(parents)

# ttt=0
for i in distinct_fitness_index:
    # ttt=1
    # for j in i.model:
    #     if j>10 or j< -10:
    #         ttt=0
    if models[i].fitness<10000000:
        f2.write(str(models[i].model))
        f2.write(" ")
        f2.write(str(models[i].err))
        f2.write("\n")
f2.close()

for j in range(100):
    print(j+1,end=' ')
    print(distinct_fitness_index[j],end=' ')
    print(models[distinct_fitness_index[j]].err ,end=' ')
    print(models[distinct_fitness_index[j]].fitness)


# print("[",end='')
# for j in range(35):
#     print(models[distinct_fitness_index[j]].model ,end=' ')
#     print(",",end='')
# print("]")


f.close()