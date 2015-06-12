from matplotlib import pyplot
import random


def roll_die(num_sides):
    'simulates rolling a die'
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

        statistical_prb = 1 / 6
        computed_prb = side_count / num_trials
        diff_data.append(computed_prb - statistical_prb)
        num_trials_data.append(num_trials)

    pyplot.plot(num_trials_data, diff_data)
    pyplot.xlabel("Number of trials ran on dice.")
    pyplot.ylabel("Difference between expected and computed results")
    pyplot.grid(True)
    pyplot.ylim((-0.5, 0.5))
    pyplot.title("Fairness of a Die in Python")
    pyplot.show()

plot_fairness_line(6, 2000, 10, 2)


def plot_fairness_bar(num_sides, num_trials):
    '''rolls the die for "num_trials" times and calculates the number of
    times each side of the die was shown, it then shows a bar plot'''
    data = {key: 0 for key in range(1, num_sides + 1)}
    for dummy_idx in range(num_trials):
        data[roll_die(num_sides)] += 1

    x_data = [key for key in data.keys()]
    y_data = [value for value in data.values()]

    pyplot.bar(x_data, y_data, width=0.3, align='center')
    pyplot.title("Fairness of a Die in Python")
    pyplot.xlabel("side of the die")
    pyplot.ylabel("Number of times the number produced")
    pyplot.grid(True)
    pyplot.show()

plot_fairness_bar(6, 3000)
