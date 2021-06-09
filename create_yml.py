import sys
import os

build_number = sys.argv[1]
job_name = sys.argv[2]
input1 = sys.argv[3]

#my_folder = '/var/jenkins_home/workspace/Continuous_Integration/'+job_name+'/config/'
#if not os.path.exists(my_folder):
# os.makedirs(my_folder)

varFileName = 'input.yml'
print(varFileName)
outfile = open(varFileName, 'w+')

outfile.write("build_number: "+build_number+ '\n')
outfile.write("job_name: "+job_name+ '\n')
outfile.write("input1: "+input1+ '\n')

outfile.close()
