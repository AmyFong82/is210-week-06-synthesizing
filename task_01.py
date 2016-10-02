#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A function calculating total no. of guests and tables for a party."""


def get_party_stats(families, table_size=6):
    """To calculate a total headcount and total number of tables needed.

    Args:
        families (list): a list of families, inside which are lists of members.
        table_size (int, optional): the maxium number of seat at each table.
                                    Default: 6

    Returns:
        tuple: total number of guests, total number of tables

    Examples:
        >>> get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack','Janis']])
        (6, 3)

        >>> get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack']], 2)
        (5, 3)
    """
    total_guests = 0
    total_tables = 0
    for guests in families:
        total_guests += len(guests)
        total_tables += -(-len(guests) // table_size)
    return (total_guests, total_tables)
