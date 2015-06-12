#! /bin/python2
#  die-probability.py: a collection of tests about the theory of probability
#  see: http://alimsvi.ir/blog/posts/ehtemal-dar-python-1.html

# Copyright (c) 2015 Ali Mousavi
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from matplotlib import pyplot
import random


def roll_die(num_sides, true_random=False):
    '''simulates rolling a die, if true_random is set, it will use random.org
    to produce true random numbers. be careful though, it might take a lot
    of time and the difference is really not that much.'''
    if true_random is True:
        import randomdotorg
        r = randomdotorg.RandomDotOrg('alimsvi.ir')
        return r.randrange(1, num_sides + 1)
    return random.randrange(1, num_sides + 1)


def plot_fairness_line(num_sides, max_trials, step, side):
    '''tests the difference between expected average and the real average
    produced after rolling a die for a range of trials.'''
    diff_data = []
    num_trials_data = []
    for num_trials in range(1, max_trials, step):
        side_count = 0
        for dummy_idx in range(num_trials):
            result = roll_die(num_sides)
            if result == side:
                side_count += 1

        statistical_prb = 1.0 / 6
        computed_prb = side_count / float(num_trials)
        diff_data.append(computed_prb - statistical_prb)
        num_trials_data.append(num_trials)

    pyplot.plot(num_trials_data, diff_data)
    pyplot.xlabel("Number of trials ran on dice.")
    pyplot.ylabel("Difference between expected and computed results")
    pyplot.grid(True)
    pyplot.ylim((-0.5, 0.5))
    pyplot.title("Fairness of a Die in Python")
    pyplot.show()

plot_fairness_line(6, 10000, 10, 2)


def plot_fairness_bar(num_sides, num_trials, true_random=False):
    '''rolls the die for "num_trials" times and calculates the number of
    times each side of the die was shown, it then shows a bar plot'''
    data = {key: 0 for key in range(1, num_sides + 1)}
    for dummy_idx in range(num_trials):
        data[roll_die(num_sides, true_random)] += 1

    x_data = [key for key in data.keys()]
    y_data = [value for value in data.values()]

    pyplot.bar(x_data, y_data, width=0.3, align='center')
    pyplot.title("Fairness of a Die in Python")
    pyplot.xlabel("side of the die")
    pyplot.ylabel("Number of times the number produced")
    pyplot.grid(True)
    pyplot.show()

plot_fairness_bar(6, 3000)
plot_fairness_bar(6, 3000, true_random=True)
