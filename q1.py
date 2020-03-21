# Python3 program to create target string, starting from 
# random string using Genetic Algorithm 

import random
import os

# Number of individuals in each generation 
POPULATION_SIZE = 10
TARGET_LENGTH = 11

# Valid genes
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP 
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

# Target string to be generated
TARGET = "I love GeeksforGeeks"







def get_error(file,child_chromosome):
	# err_value = []

	## here the child_chromosome is sent to the server and err_value receives the list of error.
	## err_value = get_errors() // blah blah whatever has to be written

	file.write("Child Generated" + child_chromosome + "\n")
	file.write("Errors Received" + err_value+"\n")
	
	return err_value










class Individual(object):
	'''
	Class representing individual in population
	'''
	def __init__(self, chromosome,err_value):
		self.chromosome = chromosome
		# self.err_value = err_value
		self.fitness = self.cal_fitness(err_value)

	@classmethod
	def mutated_genes(self):
		'''
		create random genes for mutation
		'''
		global GENES
		gene = random.choice(GENES)
		return gene

	@classmethod
	def create_gnome(self):
		'''
		create chromosome or string of genes
		'''
		global TARGET_LENGTH
		gnome = []
		gnome_len = TARGET_LENGTH
		for i in range (gnome_len):
			gene = self.mutated_genes()
			gnome.append(gene)
		
		return gnome
		# return [self.mutated_genes() for _ in range(gnome_len)]

	

	def mate(self, par2):
		'''
		Perform mating and produce new offspring
		'''

		# chromosome for offspring
		child_chromosome = []
		for gp1, gp2 in zip(self.chromosome, par2.chromosome):

			# random probability 
			prob = random.random()

			# if prob is less than 0.45, insert gene 
			# from parent 1 
			if prob < 0.45:
				child_chromosome.append(gp1)

			# if prob is between 0.45 and 0.90, insert 
			# gene from parent 2 
			elif prob < 0.90:
				child_chromosome.append(gp2)

			# otherwise insert random gene(mutate), 
			# for maintaining diversity 
			else:
				child_chromosome.append(self.mutated_genes())

			## here the child_chromosome is sent to the server and err_value receives the list of error.
			## err_value = get_errors() // blah blah whatever has to be written

			# err_value = []
    		# file.write(child_chromosome + "\n")
			# file.write(err_value+"\n")
			# file.write("\n")
		
		return child_chromosome


		# create new Individual(offspring) using 
		# generated chromosome for offspring 
		# return Individual(child_chromosome,err_value)

	def probability(self):
		'''
		To calculate the probabilty
		'''
		pass

	def cal_fitness(self,err_value,file):
		'''
		Calculate fittness score, it is the number of 
		characters in string which differ from target 
		string.
		'''
		# pass
		# global TARGET
		fitness = 0
		# for gs, gt in zip(self.chromosome, TARGET):
		 	# if gs != gt: fitness+= 1
		fitness = err_value[0] + err_value[1]
		# file.write("Fitness score" + fitness + "\n")
		# file.write("\n")

		return fitness

# Driver code 
def main():

	file = open("models.txt" , "w")
	
	global POPULATION_SIZE
	#current generation
	generation = 1
	found = False
	first_individual = [-0.00016927573251173823, 0.0010953590656607808, 0.003731869524518327, 0.08922889556431182, 0.03587507175384199, -0.0015634754169704097, -7.439827367266828e-05, 3.7168210026033343e-06, 1.555252501348866e-08, -2.2215895929103804e-09, 2.306783174308054e-11]
	## what i have understood is that population is an array of objects
	population = []

    
    ## now the population has 1 single individual (given in the question)


	## I don't know what Individual is doing here. I wrote it bcz it was written below in the for loop
	err_value = get_error(file,first_individual)
	population.append(Individual(first_individual,err_value))


	## Changed to (population_size - 1) bcz we have already added an individual
	# create initial population
	for _ in range(POPULATION_SIZE - 1):
		gnome = Individual.create_gnome()
		err_value = get_error(file,gnome)
		population.append(Individual(gnome,err_value))
		
	while not found:
		#sort the population in increasing order of fitness score
		population = sorted(population, key = lambda x:x.fitness)

		# if the individual having lowest fitness score ie. 
		# 0 then we know that we have reached to the target 
		# and break the loop
		
		if population[0].fitness <= 0:
			found = True
			break
        # Otherwise generate new offsprings for new generation

		new_generation = []
        # Perform Elitism, that mean 10% of fittest population
        # # goes to the next generation
		s = int((10*POPULATION_SIZE)/100)
		new_generation.extend(population[:s]) 

		# From 50% of fittest population, Individuals 
		# will mate to produce offspring
		s = int((90*POPULATION_SIZE)/100)
		for _ in range(s):
			parent1 = random.choice(population[:5])
			parent2 = random.choice(population[:5])
			child = parent1.mate(parent2)
			err_value = get_errors(file,child)
			# new_child = Individual(child,err_value)
			new_generation.append(Individual(child,err_value))
            
		population = new_generation 

		# print("Generation: {}\tString: {}\tFitness: {}".\ 
		# 	format(generation, 
		# 	"".join(population[0].chromosome), 
		# 	population[0].fitness))

		generation += 1

	# print("Generation: {}\tString: {}\tFitness: {}".\ 
	# 	format(generation, 
	# 	"".join(population[0].chromosome), 
	# 	population[0].fitness)) 

if __name__ == '__main__': 
	main() 
