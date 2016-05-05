#!/usr/bin/env python

import glob, os, yaml, re

d='.'
folders = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))];
folders.sort()

def extractFunctions(searchText):
    return re.findall("((void|bool|int|float|vec\\d|mat\\d)+\\s.*\\(.*\\)\\s+\\{)", searchText)

readmes = []

# FOLDER
for folder in folders:
    readme = folder+'/README.md'
    readme_file = open(readme, "w")

    for filename in glob.glob(folder+'/*.yaml'):
        yaml_file = yaml.safe_load(open(filename))
        for name_block in yaml_file['styles']:
            url = 'https://github.com/tangrams/blocks/blob/gh-pages'+filename[1:]

            readme_file.write('\n\n### [' + name_block + ']('+url+')\n\n');

            if 'doc' in yaml_file['styles'][name_block]:
                if 'description' in yaml_file['styles'][name_block]['doc']:
                    readme_file.write(yaml_file['styles'][name_block]['doc']['description'])

                readme_file.write(  '\n\nImport it using:\n\n' +
                                    '```yaml\n' +
                                    'import:\n' +
                                    '    - http://tangrams.github.io/blocks/' + folder + filename + '\n' +
                                    '```\n\n')

            if 'shaders' in yaml_file['styles'][name_block]:
                if 'blocks' in yaml_file['styles'][name_block]['shaders']:
                    readme_file.write('Provides the following blocks:\n');
                    for block in yaml_file['styles'][name_block]['shaders']['blocks'].keys():
                        readme_file.write('\n- **' + block + '**:')

                        if block == 'global':
                            functions = extractFunctions(yaml_file['styles'][name_block]['shaders']['blocks'][block])
                            for function in functions:
                                readme_file.write('\n + `' + function[0][:-1] + '`')
                        else:
                            readme_file.write(  '\n\n```glsl\n' + 
                                                yaml_file['styles'][name_block]['shaders']['blocks'][block] +
                                                '\n```\n\n')
            readme_file.write('\n')
    readme_file.close()
    readmes.append(readme)
    
with open('README.md', 'w') as outfile:
    with open('INTRO.md') as infile:
            outfile.write(infile.read())

    for fname in readmes:
        with open(fname) as infile:
            outfile.write(infile.read())

    outfile.write('\n## License\n')
    with open('LICENSE.md') as infile:
            outfile.write(infile.read())

