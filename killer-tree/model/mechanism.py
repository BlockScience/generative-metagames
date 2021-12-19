from scipy.stats import bernoulli

def is_Tree_Sick(params, step, prev_state, state, _input):
    
    prior = params['prior_tree_sick']

    poison_tree = state['Alice']['Poison Tree Decision']
    poison_strength = params['poison_stregth']

    posterior = prior + (1-prior)*poison_strength*poison_tree

    print("The likelihood the tree get's sick is "+str(posterior))
    outcome = bernoulli.rvs(posterior)

    print("The outcome for the tree getting sick is "+ str(outcome))

    world = state['World']
    world['Tree Sick Outcome'] = outcome

    return ("World", world)

def is_Tree_Dead(params, step, prev_state, state, _input):
    
    prior = state['World']['Tree Sick Outcome']

    tree_doctor = state['Bob']['Tree Doctor Decision']
    doctor_skill = params['doctor_skill']

    posterior = prior*(1- doctor_skill*tree_doctor)

    print("The likelihood the tree dying is "+str(posterior))
    outcome = bernoulli.rvs(posterior)

    print("The outcome for the tree dying sick is "+ str(outcome))

    world = state['World']
    world['Tree Dead Outcome'] = outcome

    return ("World", world)

def resolve_Poison_Tree(params, step, prev_state, state, _input):

    poison = _input['poison']

    alice = state['Alice']
    alice['Poison Tree Decision'] = poison

    alice['Effort Utility'] = poison * params['alice_payoffs']['effort']

    return ("Alice", alice)


def resolve_Tree_Doctor(params, step, prev_state, state, _input):

    doctor = _input['doctor']

    bob = state['Bob']
    bob['Tree Doctor Decision'] = doctor

    bob['Cost Utility'] = doctor * params['bob_payoffs']['cost']

    return ("Bob", bob)

def resolve_Build_Patio(params, step, prev_state, state, _input):

    build = _input['build']

    alice = state['Alice']
    alice['Build Patio Decision'] = build

    return ("Alice", alice)

def resolve_Alice(params, step, prev_state, state, _input):

    alice = state['Alice']
    world = state['World']

    dead_tree = world["Tree Dead Outcome"]

    alice['View Utility'] = dead_tree*alice['Build Patio Decision']*params['alice_payoffs']['view']

    observables = [alice, world]

    alice['Agent'].update_strategy(observables)

    return ("Alice", alice)

def resolve_Bob(params, step, prev_state, state, _input):

    bob = state['Bob']
    world = state['World']

    tree = 1- world["Tree Dead Outcome"]

    bob['Tree Utility'] = tree * params['bob_payoffs']['tree']

    observables = [bob, world]

    bob['Agent'].update_strategy(observables)

    return ("Bob", bob)