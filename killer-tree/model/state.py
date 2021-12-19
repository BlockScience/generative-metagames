from .behavior import Alice, Bob

genesis_state = {
    "Alice": 
    {
        "Agent": Alice(),
        "Poison Tree Decision": False, 
        "Build Patio Decision": False, 
        "Effort Utility":0, 
        "View Utility":0
    },
    "Bob": 
    {
        "Agent": Bob(),
        "Tree Doctor Decision": False,
        "Cost Utility": 0,
        "Tree Utility": 1
    },
    "World":
    {
        "Tree Sick Outcome": False,
        "Tree Dead Outcome": False
    }
}