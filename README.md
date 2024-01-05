# ScrabbleAI

## Setup and package management
Create virtual environment and install package dependencies\
`python -m pip install -r requirements.txt`

Install new package with \
`python -m pip install numpy`\
and add changes to the `requirements.txt` file with\
`python -m pip freeze > requirements.txt`

Run script with `python <path>\scrabbleai.py <args>` or `python scrabbleai.py <args>`
when being in the home directory ("ScrabbleAI") of this project.

## Linting
For linting, pylint ist used.
To lint the project, run `pylint -j 0 --recursive=y --rcfile .pylintrc src scrabbleai.py` in the terminal.

## Testing 
To run all tests, run `python -m unittest discover -s src/test -v` in the terminal.

A file that contains tests must begin with `test_` and be located in `src/test`. 
The test class must inherit from `unittest.TestCase`. 
Every test method must begin with `test_`.
   
    class SampleTestCase(unittest.TestCase):

        # Test methods ...
        def test_sample(self) -> None:
            self.assertTrue('Hello' != 'World')

## Project information
### Versions
- Python: 3.10.8
- Pip: 23.3.1