#!/usr/bin/env python

from paver.tasks import task, needs, BuildFailure
from paver.easy import sh


@task
def unit_tests():
    sh('nosetests --with-coverage tests/unit')

@task
def lettuce_tests():
    sh('lettuce tests/bdd')

@task
def run_pylint():
    try:
        sh('pylint bank/ > pylint.txt')
    except BuildFailure:
        pass


@needs('unit_tests', 'lettuce_tests', 'run_pylint')
@task
def default():
    pass
