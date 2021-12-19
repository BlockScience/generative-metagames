from .behavior import Alice, Bob

## Note: this is a repeated game
# the only state variable carried between rounds is the Agent
# therefore all other genesis states are empty
# because there should be no prior round state dependence

genesis_state = {
    "Alice": 
    {
        "Agent": Alice(),
        "Poison Tree Decision": None, 
        "Build Patio Decision": None, 
        "Effort Utility":None, 
        "View Utility":None
    },
    "Bob": 
    {
        "Agent": Bob(),
        "Tree Doctor Decision": None,
        "Cost Utility": None,
        "Tree Utility": None
    },
    "World":
    {
        "Tree Sick Outcome": None,
        "Tree Dead Outcome": None
    }
}