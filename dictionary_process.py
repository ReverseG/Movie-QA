import pandas as pd


def create_dic():
    person_csv = pd.read_csv('data/person.csv')
    person_csv['name'] = person_csv.apply(lambda x: x['name'].replace('"', ''), axis=1)
    person_csv['freq'] = '10'
    person_csv['prop'] = 'nr'
    person = person_csv[['name', 'freq', 'prop']]

    movie_csv = pd.read_csv('data/movie.csv')
    movie_csv['freq'] = '10'
    movie_csv['prop'] = 'nm'
    movie = movie_csv[['title', 'freq', 'prop']]
    movie = movie.rename(columns={'title': 'name'})

    gener_csv = pd.read_csv('data/genre.csv')
    gener_csv['freq'] = 10
    gener_csv['prop'] = 'ng'
    gener = gener_csv[['gname', 'freq', 'prop']]
    gener = gener.rename(columns={'gname': 'name'})

    dic = pd.concat([person, gener, movie])
    dic = dic.reset_index(drop=True)
    dic.to_csv('./data/dictionary.csv', header=False, index=False, sep=" ")


if __name__ == '__main__':
    create_dic()
    s = '"Chen Dao-Ming"'
    print(s.replace('"', ''))
