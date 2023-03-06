from itertools import permutations
import os
import keyboard


def kill_button():
    while True:
        if keyboard.is_pressed('x'):
            print(" -kill button ended program")
            os._exit(0)
            break


def unique_groupings(length, unique_ints):
    if length == 1:
        groupings = [[i] for i in unique_ints]
    elif length > 1:
        groupings = list(permutations(unique_ints, length))
        groupings = [list(item) for item in groupings]
    else:
        return []
    return groupings


def calculate_support(unique_groups, transaction_list, do_print=True):
    # calculates the support for each item in unique_groups for appearance within items of order_list
    result = []
    for group in unique_groups:
        count = 0
        for transaction in transaction_list:
            if all(x in transaction for x in group):
                count += 1
        if do_print:
            print(f"Item:{group}, Support: {round(count / len(transaction_list), 2)}")
        result.append(count / len(transaction_list))
    return result


def drop_check(calculated_supports, support_threshold, unique_groups):
    supported_groups = []
    for i, support in enumerate(calculated_supports):
        if support < support_threshold:
            print(f"dropping{unique_groups[i]}")
        else:
            supported_groups.append(unique_groups[i])
    return supported_groups


def calculate_confidence(unique_groups, transaction_list, do_print=True):
    # returns an array of confidence values for the unique groups
    result = []
    for group in unique_groups:
        X = group[:-1]  # everything but the last element
        Y = group[-1]  # the last element
        xy_count = 0  # appearance of X and Y together
        x_count = 0  # appearance of just X
        for transaction in transaction_list:
            if all(Xi in transaction for Xi in X):
                x_count += 1
                if Y in transaction:
                    xy_count += 1
        # calculate confidence
        if(x_count == 0):
            confidence = 0
        else:
            confidence = (round(xy_count / x_count, 2))
        result.append(confidence)
        if do_print:
            print(f"Item:{X}-> {Y}, Confidence: {round(confidence,2)}")

    return result


def new_rules(unique_groups, transaction_list):
    supports = calculate_support(unique_groups, transaction_list, do_print=False)
    confidence = calculate_confidence(unique_groups, transaction_list, do_print=False)
    new_rules = []
    my_dict = {}

    # first put all the rules together, the premise, the conclusion, and the support and confidence for them.
    for i, group in enumerate(unique_groups):
        my_dict[tuple(sorted(group[:-1]))] = (group[-1], supports[i], confidence[i])

    # we add the rule only if it is not a duplicated rule
    # this will make sure we do not have duplicated rules ie(1,2) implies 3 is the same as (2,1) implies 3
    for key in my_dict:
        value = my_dict[key]
        new_rules.append(f"{list(key)} -> {value[0]} | Support: {value[1]} Confidence: {value[2]}")
        print(f"NEW RULE: {list(key)} -> {value[0]} | Support: {value[1]} Confidence: {value[2]}")
    return new_rules
