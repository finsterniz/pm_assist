#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 24.06.23 10:38 am
# @Author  : Hao
# @File    : test_add_stricht.py

import re

def process_text(text):
    lines = text.split('\n')
    new_lines = []
    add_hyphen = False

    for line in lines:
        if re.match(r"Pros:|Cons:", line):
            add_hyphen = True
            new_lines.append(line)
        elif line.strip() == "":
            add_hyphen = False
            new_lines.append(line)
        elif add_hyphen:
            new_lines.append("- " + line)
        else:
            new_lines.append(line)

    return '\n'.join(new_lines)

input_text = '''
You are a process mining expert, your task is to give some possible redesign Output based on Input Case, please follow the EXAMPLE below, and give a redesign Output for the <Input Case> I gave.
---
EXAMPLE
<Input Case>: 
In a university registrar’s office processes, employee manually enters students’ data into the system. Which lead to long processing times.
<Output Redesign>: 
1 Hire more staff to handle the process.
2 The students are to enter their personal data into the system themselves. 
3 The data entry activities can be automated, for instance performed automatically by the system itself.
---\n
<Input Case>: 



now you will read some heuristics for redesign, and determine which 3 heuristics are applicable
---
HEURISTICS
4.3.4 Exception

Definition: 
Designing business processes primarily for typical orders while isolating exceptional orders. This prevents exceptions from disrupting normal operations and potentially allows for specialized expertise development in handling exceptions.

Pros:
Better Efficiency of normal orders 
Better Overall performance  (possible, if specialized expertise is developed)

Cons:
Less Flexibility
Higher Cost due to the need for specialized expertise in handling exceptions


4.6.2 Integral technology
Definition:
Integral technology in business processes involves applying new technology to overcome physical constraints, potentially resulting in efficiency gains and enabling new possibilities for how business is conducted.

Pros:
less time spent on logistical tasks 
better quality of service 
more possibilities for business 

Cons:
more purchase, development, implementation, training, and maintenance costs
may cause fear or resistance from workers


4.7.3 Interfacing

Definition:
Interfacing involves using a standardized interface for streamlined communications with customers and partners, and for maintaining data accuracy through regular database reviews and cleansing. This aims to enhance efficiency and data quality.

Pros:
better quality 
less processing time
less rework cost


2.2 Task elimination

Definition: 
Task elimination is a strategy that involves removing unnecessary tasks from a business process. A task is generally considered unnecessary if it adds no value from the customer's point of view. Redundant tasks and control tasks are often subject to elimination.

Pros:
increase processing speed 
lower cost 

Cons:
service quality might decline


4.1.2 Flexible assignment

Definition: 
Flexible assignment is a strategy where resources are assigned tasks in a manner that maximizes flexibility for the near future. For instance, if a task can be done by either of two available resources, it is assigned to the most specialized resource. This preserves the availability of the more general resource for other tasks.

Pros:
queue time reduce
better quality

Cons:
potential work load imbalance
less job satisfaction
less career growth opportunities for specialists


4.7.2 Outsourcing

Definition:
Outsourcing involves delegating a business process or parts of it to a third party who might perform it more efficiently. This can include tasks like customer service, manufacturing, or data processing.

Pros:
less cost
better quality

Cons:
more coordination efforts
may make business process more complex


3.3 Parallelism

Definition: 
Parallelism refers to the practice of executing tasks in parallel, as opposed to sequentially, in a business process. This strategy can substantially reduce the throughput time of a process.

Pros:
less throughput time

Cons:
more cost
more complex of managing concurrent tasks
Potential quality decline
less flexibility


3.2 Knock-out

Definition: 
Knock-out involves ordering tasks in a decreasing order of effort and an increasing order of termination probability. It focuses on tasks that check various conditions needed for a positive result in the business process. Any unmet condition can lead to termination, or "knock-out" of that part of the process. In example “Early termination”: immediately stopping the process at its initial stages if key conditions are not met, in order to save resources.

Pros:
reduce business process execution cost

Cons:
less freedom of task ordering
less throughput time


4.1.5 Customer Teams

Definition: 
The practice of customer teams involves assigning teams consisting of workers from different departments to handle specific types of orders. This is a variation of the order assignment practice and can result in more workers with similar qualifications working on the same tasks, easing the Inflexibility of the order assignment practice.

Pros:
Similar to the order assignment best practices:
better Quality (improved work attractiveness and understanding)
less Setup time
better service quality

Cons:
less flexibility of resource allocation
more Queue time + (if the assigned person is not available)

4.2.1.1 Specialist

Definition: 
This heuristic involves adjusting the ratio of specialists through training or hiring. Employees may be turned from generalists into specialists.
Specialists are likely to develop a routine more quickly and have deeper knowledge, leading to quicker work and higher quality.

Pros:
The purpose of this heuristic is to gain speed.


4.2.1.2 Generalist

Definition: 
This heuristic involves increase the ratio of generalists through training or hiring. Employees may be turned from specialists into generalists.
Generalists add flexibility to the business process and can lead to better resource utilization.

Pros:
The purpose of this heuristic is to gain flexibility.


4.5.1 Control addition

Definition:
Control addition involves integrating checks into a business process to ensure the completeness and correctness of incoming materials as well as verifying the output before it is sent to customers.

Pros:
better quality of business process execution
less rework required

Cons:
more time required for additional control
require additional time and resources


4.7.1 Trusted party

Definition:
Using a trusted party involves relying on information or assessments provided by a reputable third party, rather than independently verifying or generating the information. For example, accepting a creditworthiness certificate from another bank instead of assessing a customer's creditworthiness internally.

Pros:
less cost
less throughput time

Cons:
more dependency on another party's quality
more coordination effort with trusted parties
less flexibility


4.3.1 Resequencing

Definition: 
This is the process of rearranging tasks to optimize the order in which they're performed. This could involve postponing certain tasks or placing similar tasks closer together to reduce setup times.

Pros:
less cost
less Setup time


4.2 Extra resources

Definition: 
This practice refers to increasing the number of resources when capacity is insufficient to handle orders. This means adding more staff, tools, or other types of resources to improve capacity and potentially flexibility.

Pros:
Reduces queue time
Enhances flexibility of assignment policy


Cons:
Higher cost due to hiring or acquiring extra resources.


4.1.6 Numerical involvement

Definition: 
Minimizing the number of departments, groups, and individuals involved in a business process. The goal of this practice is to reduce the amount of time spent coordinating tasks and responsibilities among a large number of people or departments.

Pros:
less coordination problems
more time available for order processing
less Potential reduction of split responsibilities

Cons:
Potential obstruction to expertise and routine development due to fewer specialized units.


1.3 Integration

Definition: 
Integration refers to the practice of combining or connecting the business processes of a company with those of its customers or suppliers. It takes inspiration from the supply-chain concept and may take different forms depending on the specific scenario. 

Pros:
more execution efficiency (time and cost)

Cons:
increased mutual dependence
less flexibility


4.5.2 Buffering


Definition:
Buffering in business processes means subscribing to updates from external sources, instead of actively requesting information each time. This ensures that information is readily available when needed, similar to caching in microprocessors.

Pros:
less throughput times

Cons:
additional subscription fees
more cost of storing information


2.5 Task composition or decomposition

Definition: 
Task composition involves combining small tasks into larger, composite tasks, and decomposition dividing large tasks into smaller, more manageable tasks. This strategy seeks to reduce setup times and improve the quality of work, while also maintaining task manageability and flexibility.

Pros:
less setup times
better quality of work

Cons:
less runtime flexibility
less task manageability


1.1 Control relocation

Definition: 
Control relocation refers to the practice of shifting checks and reconciliation operations from the business to the customer side in a business process. For example, supermarket self-service payment.

Pros:
less billing errors
more customer satisfaction

Cons:
more yield


2.3 Order-based work

Definition: 
This practice suggests removing batch-processing and periodic activities from a business process. Thereby significantly speeding up the processing of individual orders.

Pros:
speed up individual order handling

Cons:
less scale efficiencies
more cost of maintaining information system


4.1.4 Split responsibilities

Definition: 
Split responsibilities is a business practice that encourages avoiding task assignments to people from different functional units. The idea is to reduce the overlap in responsibilities, which can often lead to neglect and conflict, thereby improving task execution quality and responsiveness.

Pros:
better task execution quality
faster responsiveness
less throughput time

Cons:
potential for increased queuing


4.1.7 Case Manager

Definition: 
This heuristic involves appointing one person as responsible for the handling of each type of order. This person, the case manager, is responsible for a specific order or customer but does not necessarily perform the tasks related to it. The focus is on the management of the process rather than its execution.

Pros:
Improved external business process quality
Increased customer satisfaction
Potential improvement in internal quality due to accountability

Cons:
increased costs


4.2.2 Empower

Definition:
Empowerment in business processes means granting workers the authority to make decisions, reducing the reliance on middle management for authorizations.

Pros:
less throughput times
reduce labor cost 

Cons:
potential worse quality of decisions
more cost of handling orders (in case of errors or bad decisions)


4.4.1 Order assignment

Definition: 
This practice involves letting workers perform as many steps as possible for a single order. This reduces the setup time as the resource will be acquainted with the case, possibly improving service quality. However, this can significantly decrease the flexibility of resource allocation.

Pros:

less Setup time
better service quality

Cons:
less flexibility of resource allocation
more Queue time + (if the assigned person is not available)


2.1 Order types

Definition: 
The concept of "Order Types" involves identifying whether tasks are associated with the same type of order and, if necessary, creating new separate business processes. This practice highlights the importance of not ignoring subflows that are not specific to the business process they are part of.

Pros:
less processing times
more cost
better efficiency

Cons:
more coordination problems
less flexibility


1.2 Contact reduction

Definition: 
By reducing the number of contacts, you can save time and increase efficiency. Because exchanging information with customers or third parties is often time-consuming.

Pros:
less throughput time
better quality


4.1.3 Centralization

Definition: 
Centralization refers to treating geographically dispersed resources as if they are centralized, often facilitated by a Workflow Management System (WfMS). It's aimed at reaping the benefits of technology to manage work assignments without considering geographical locations.

Pros:
better resource utilization
less throughput time
more flexibility

Cons:
may include more cost, complexity, and issues with adaptation


4.2.4 Triage

Definition: 
This involves redefining tasks to align with resource capabilities and order characteristics. It can be through splitting a general task into alternative ones, or merging alternative tasks into a general one. Another form of triage is dividing a task into similar tasks for different order subcategories.

Pros:
better Quality
better Resource utilization
less Cost
less Time

Cons:
less Flexibility
more Work monotony


4.6.1 Task automation

Definition:
Task automation involves using technology to perform tasks that were previously done manually, with the aim of executing them faster, at a lower cost, and with better results.

Pros:
execution speed up
reduce cost of task execution
better quality of results

Cons:
more development cost of automation system
less flexibility in handling variations


8.1 Workload Management

Definition:
"Workload Management" is the process of effectively distributing tasks among team members or across an organization to optimize productivity and prevent burnout. It involves monitoring workloads, prioritizing tasks, and assessing team capacity.

Pros:
Increased Productivity
Prevents Burnout
Optimizes Resource Utilization

Cons:
Time-Consuming
Potential for Conflict
Requires Dynamic Adjustments


8.2 Process Standardization

Definition:
Process standardization refers to the creation and implementation of consistent, standardized processes and rules to ensure efficiency and consistency in business operations. This typically includes defining clear steps, tasks, responsibilities and standards to guide workflow within the organization.

Pros:
Better Efficiency
Better Quality
easier to teach

Cons:
Over-standardization lead to inflexibility
less creativity


8.3 Continuous Improvement

Definition:
Continuous improvement is a strategy emphasizing regular evaluation and enhancement of an organization's performance and processes.

Pros:
Increases efficiency and effectiveness.
Improves employee and customer satisfaction.

Cons:
May lead to over-optimization.
Requires time and resources.


8.4 Advocacy Management

Definition:
Advocacy management involves actively promoting and encouraging change to drive organizational progression and development.

Pros:
Fosters innovation and change.
Enhances employee engagement.

Cons:
May face resistance.
Requires strong leadership.

8.5 Forecasting

Definition:
Forecasting predicts factors like customer demand, production, inventory, logistics, and risks, informing planning of business activities.

Pros:
Aids strategic planning.
Minimizes risks.
Reduces costs.

Cons:
Inherent uncertainty.
Requires resources and expertise.
Dependent on data quality.

8.6 Cross-functional Collaboration

Definition:
Cross-functional collaboration is when employees from different functions or departments work together towards a common goal or project.

Pros:
Enhances innovation.
Improves efficiency.

Cons:
Communication and coordination challenges.
Potential for conflicts.


'''

output_text = process_text(input_text)
print(output_text)
