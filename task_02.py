#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A function to send email reminders to clients about their appointments."""


def prepare_email(appointments):
    """To send email reminders to clients about their appointments.

    Args:
        appointments (list): a list of clients name and appointment in tuples.

    Returns:
        list: A new list with each client's email body containing their name
              and appintment.

    Examples:
        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')]
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']

        >>>prepare_email([('Amy', '2016'), ('Kay', 'Sept 4')])
        ['Dear Amy,\nI look forward to meeting with you on 2016.\nBest,\nMe',
        'Dear Kay,\nI look forward to meeting with you on Sept 4.\nBest,\nMe']
    """
    email = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    newlist = []
    for clients in appointments:
        new_email = email.format(clients[0], clients[1])
        newlist.append(new_email)
    return newlist
