[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15607543.svg)](https://doi.org/10.5281/zenodo.15607543)

# First steps in statistics for life science - with python

Statistics are an integral aspect of scientific research, particularly for the life sciences which rely heavily on quantitative methodologies. 
This course is designed to provide researchers in the life sciences with a gentle introduction to statistics and its application to a variety of biological problems.

This course is intended for scientists (and in particular life scientists) from all levels and disciplines who are not experts in statistics. 

Although we will provide materials and a reminder on data mamipulation in python, participant must be comfortable with the python environment and be able to read, understand and write basic python commands before attending this course. We also recommend some familiarity with the pandas, and matplotlib libraries.

The course will combine lectures on statistics, short tutorials and practical exercises on the topics discussed in the class. These practical exercises will be implemented in the widely used python language and environment for statistical computing and graphics.

## Technical prerequisites

Software to be installed **prior** to the course:

- **Miniconda** — package manager and environment management system ([install guide](https://www.anaconda.com/docs/getting-started/miniconda/install/overview))

### Setting up the environment

Create a conda environment from the provided `environment.yml` file:

```bash
conda env create -f environment.yml
```

The file specifies the environment name, package channels, and dependencies:

```yaml
name: statistics_sib
channels:
  - defaults
  - conda-forge
dependencies:
  - python=3.14.3
  - pandas=3.0.2
  - scipy=1.17.1
  - seaborn=0.13.2
  - jupyter=1.1.1
  - scikit-learn=1.8.0
  - plotly=6.6.0
  - statsmodels=0.14.6
  - anndata=0.12.11
```

## Course Schedule

### Day 1

#### Morning

| Time | Session | Type | Duration |
|------|---------|------|----------|
| 09:30 – 09:40 | Welcome & course overview | Intro | 10 min |
| 09:40 – 10:10 | **Lecture 1** — Data Visualisation & Exploration | Lecture | 30 min |
| 10:10 – 11:40 | **Exercises** — [Notebook 1](01_EDA.ipynb) | Exercises | 90 min |
| 11:40 – 12:40 | Lunch | — | 1 h |

#### Afternoon

| Time | Session | Type | Duration |
|------|---------|------|----------|
| 12:40 – 14:10 | **Lecture 2** — Distributions & Hypothesis Testing | Lecture | 90 min |
| 14:10 – 15:10 | **Exercises** — [Notebook 2a](02_distribution_and_statistical_tests.ipynb) | Exercises | 1 h |
| 15:10 – 15:25 | Break | — | 15 min |
| 15:25 – 16:25 | **Exercises** — [Notebook 2b](02_distribution_and_statistical_tests.ipynb) | Exercises | 1 h |

---

### Day 2

#### Morning

| Time | Session | Type | Duration |
|------|---------|------|----------|
| 09:30 – 10:30 | **Lecture 3** — Statistical Testing, Continued | Lecture | 1 h |
| 10:30 – 11:15 | **Exercises** — [Notebook 3a](03_distribution_and_statistical_tests_continued.ipynb) | Exercises | 45 min |
| 11:15 – 11:30 | Break | — | 15 min |
| 11:30 – 12:15 | **Exercises** — [Notebook 3b](03_distribution_and_statistical_tests_continued.ipynb) | Exercises | 45 min |

#### Afternoon

| Time | Session | Type | Duration |
|------|---------|------|----------|
| 13:15 – 13:45 | **Lecture 4** — Correlation & Regression | Lecture | 30 min |
| 13:45 – 14:45 | **Exercises** — [Notebook 4a](04_correlation_and_regression.ipynb) | Exercises | 1 h |
| 14:45 – 15:00 | Break | — | 15 min |
| 15:00 – 16:00 | **Exercises** — [Notebook 4b](04_correlation_and_regression.ipynb) | Exercises | 1 h |


## Course organization

The course is organized in several, numbered, jupyter notebooks, each corresponding to a chapter which interleaves theory, code demo, and exercises.

The course does not require any particular expertise with jupyter notebooks to be followed, but if it is the first time you encounter them we recommend this [gentle introduction](https://realpython.com/jupyter-notebook-introduction/).

 * [01_data_manipulation_and_representation.ipynb](01_data_manipulation_and_representation.ipynb) : an introduction without much statistics, to get everyone up to speed on the pandas, matplotlib, and seaborn libraries. 
 * [02_distribution_and_statistical_tests.ipynb](02_distribution_and_statistical_tests.ipynb)
 * [03_distribution_and_statistical_tests_continued.ipynb](03_distribution_and_statistical_tests_continued.ipynb)
 * [04_correlation_and_regression.ipynb](04_correlation_and_regression.ipynb)


Solutions to each practical can be found in the `solutions/` folder and should be loadable directly in the jupyter notebook themselves.

## Citation

Please cite as:
Wandrille Duchemin. (2025, June 6). Material for the "Introduction to Statistics with Python" SIB-training course adapted for a self-learning experience. Zenodo. https://doi.org/10.5281/zenodo.15607543
