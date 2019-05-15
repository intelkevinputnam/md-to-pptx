import os

file = 'plugin-list'
gitPrefix = 'git@github.com:intel/'
gitSuffix = '.git'
absPath = os.path.abspath(__file__)
homeDir = os.path.dirname(absPath)
numFiles = 0


with open(file) as f:
    plugins = f.readlines()

for line in plugins:
    args = line.split()
    gitDir = args.pop(0)

    #clone the repo
    os.system('git clone ' + gitPrefix + gitDir + gitSuffix)

    #generate docx for all readmes associated with repo
    for readmePath in args:
        os.chdir(os.path.dirname(gitDir + "/" + readmePath))
        outputFileName = 'readme' + str(numFiles) + '.docx'
        os.system('pandoc ' + os.path.basename(readmePath) + ' -o ' + outputFileName)
        os.system('mv ' + outputFileName + ' ' + homeDir)
        os.chdir(homeDir)

        numFiles += 1

#merge all resulting docx files into a single docx
os.system('pandoc readme*.docx -o final.docx')