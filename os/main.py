import os

path = os.getcwd() # Current Path

print(path)

os.chdir("../") # Changing current path

path = os.getcwd() # Current Path

print(path)


# ---------------------------------
# Creating directory

directory = "ProjectsforGithub"
parent_dir = "C:/"
path = os.path.join(parent_dir, directory)
mode = 0o666 # Read and Write permissions

os.mkdir(path, mode) # Creating directiory with mkdir
print("Directory '% s' created" % directory)

print(os.listdir(path)) # listando os arquivos do diretorio




