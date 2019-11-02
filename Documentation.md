# MEC

## Description

We decided to address the wait times for both paying and buying food at La
Piazza. To address this issue, we implemented a system for customers to take
tickets when they enter, connect the tickets to their purchases and then pay for
their meals all while they wait for their meal to be cooked.

## Interface

The system is split into three parts, the cook's interface (cookside), the
cashier's interface (payment) and the database that is driven by both. The
cook's interface connects a ticket number to food items and then the cashier
verifies that the ticket is valid and allows for it to be paid. After a ticket
has been paid, no new items can be put on the ticket.

### Cookside

The cook can enter a valid ticket ID and then a number of food items and they
will be connected to the ticket. For debug purposes, their interface will also
allow them to introduce new tickets into the system. In reality, a ticket will
be created when a student walks into La Piazza

### Payment
