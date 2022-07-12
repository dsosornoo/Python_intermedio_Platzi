DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    all_python_dev=[worker["name"] for worker in DATA if worker['language']=='python']
    all_platzi_workers=[worker["name"] for worker in DATA if worker['organization']=='Platzi']
    adults=[worker['name']for worker in DATA if worker['age']>18]
    olds=[{**worker,**{'odd':worker['age']>70}} for worker in DATA]
    
    adult=list(filter(lambda worker:worker["age"]>18,DATA))
    adult=list(map(lambda worker:worker["name"],adult))
    old= list(map(lambda worker: worker | {"old":worker['age']>70},DATA))
    python_dev=list(filter(lambda worker:worker['language']=='python',DATA))
    python_dev=list(map(lambda worker:worker['name'],python_dev))
    Platzi=list(filter(lambda worker:worker['organization']=='Platzi',DATA))
    Platzi=list(map(lambda worker:worker['name'],Platzi))
    
    
    for worker in Platzi:
        print(worker)

    # print('Python workers: ') 
    # for worker in all_python_dev:
    #     print(worker)
    # print("\n ") 
    # print('Platzi workers: ') 
    # for worker in all_platzi_workers:
    #     print(worker)
    # print("\n ") 

if __name__ == '__main__':
    run()