# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, with_statement
from fabric.api import local, task
from fabric.colors import green, cyan


@task
def master():
    print(cyan('Rebasing master ...'))
    local('git rebase master')

    print(cyan('Pushing master ...'))
    local('git push origin master')

    print(green('Success! Pushed to origin master'))