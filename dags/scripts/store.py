import json
import os


def store_data(articles, filename):
    # Save the articles to a file
    with open(filename, 'w') as f:
        json.dump(articles, f, indent=4)

    if not os.path.exists('.dvc'):

        os.system('dvc init')

    os.system(f'dvc add {filename}')

    os.system(f'git add {filename}.dvc .gitignore')
    os.system(f'git commit -m "Add/update {filename}"')

    # Push the file to the DVC remote
    os.system(f'dvc push {filename}')


def main(articles):
    store_data(articles, 'articles.json')


if __name__ == "__main__":
    # Example articles data
    articles = [
        {'title': 'Example Title 1', 'link': 'http://example.com/1',
            'description': 'Description 1'},
        {'title': 'Example Title 2', 'link': 'http://example.com/2',
            'description': 'Description 2'},
    ]
    main(articles)
