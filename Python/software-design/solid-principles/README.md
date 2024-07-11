# S.O.L.I.D Principles

## Single Responsibility

> A class should have a single responsibility.

If we are using the same class for Managers and who all are reporting to him just because they both are employees of the company, it will introduce unwanted impact when changes are introduced to specific for any one of them.

The end goal of this principle is to avoid any changes in one role that should not affect the other role. Otherwise, if recent changes are introduced any bugs, it will also affect the unrelated role.


## Open-Closed

> A class should be Open for extension and closed for modification.

This principle may have a little conflict over the **single-responsibility** principle, which is having a single responsibility how can we extend the role? but we must understand adding an action to a role should not change the role. so, this principle talks about it.

A `project manager` can also function as a `scrum master` and the manger is open to acting as a scrum master, but it's different from taking responsibility for a `project director`.

The end goal of this principle is to avoid, if there are any changes in a class signature that may trigger bugs in the existing implementation of that class, so extending only the action of that class might hold the backward compatibility.

## Liskov Substitution

> This principle says, as a child, you might be able to serve the purpose of your parent as a substitute.

If a class `Benz` is a subclass of Type `Car`, wherever there is a need for a `Car`, the `Benz` should be able to complete the need.

An `associate tech leader` can function as a `leader` when there is a substitution needed from the leader.

The end goal of this principle is to keep the consistency over inheritance of properties without making any compromise.

## Interface Segregation

> This principle says clients should be forced to depend on the methods that they do not use.

If a class `3GCustomer` is inheriting from a `TelecomCompany` where this company offering a recharge pack which includes the 4G Benefits, which cannot be used by the `3GCustomer`, but they still depend on the package for talk time and paying extra for this unwanted feature.

The end goal of this principle is to split the set of actions into smaller sets, which will execute actions only specific to themselves.

## Dependency inversion

This principle says:

1. High-Level module should not depend on the Low-Level module. Both should depend on the abstraction.
2. Abstraction should not depend on the details. Detail should depend on the abstractions.

> If a class `Store` (High-Level) is explicitly dependent on a `CreditCard` (Low-Level) payment processor, it will be difficult to adapt new payment modes in the future. It will also trigger unnecessary code changes in the `Store` and may lead to unwanted bugs. For avoiding this, we can create an Interface(abstraction) `PaymentProcessor` and allow every new payment mode to implement this interface like, `CreditCardPaymentProcessor` or `DebitCardPaymentProcessor` which is dependent on this abstraction. Use these same abstractions in the `Store` so that any newly introduce payment will not trigger any changes to it. Also, we need to make sure that abstraction does not explicitly depend upon any payment mode, but this payment mode details (how it works) depend on or satisfy the abstraction requirements.

The end goal of this principle is to reduce the dependency between the High-Level & Low-Level modules by introducing the interface.
