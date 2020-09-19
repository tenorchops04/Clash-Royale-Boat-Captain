# Clash-Royale-Boat-Captain
A tool for Clash Royale leaders and players to monitor their clans performance in Clan Wars 2.

## Goals
As this is a personal project of mine, I'd like to outline some goals I'd like to achieve. These may evolve as the program grows.
- For each clan, display useful information on each clan member that will allow clan leaders to better manage their clans. I'm starting with the basics such as fame and repair points.
- Build in different options and tools for clan leaders to use that allows them to find the information that they find useful. Initial ideas are:
  - Set a range to distinguish exception performers and those that may need help.
  - An option which will build the best decks for boat defense based on opponents' decks and the card levels of the player using the tool.
  - Allow the user to choose in what order to display the information:
    - Lowest to highest fame
    - Highest to lowest fame
    - Lowest to highest repair points
    - Highest to lowest repair points
  
## Current Functions
The program prompts the user for the clan tag, which must exclude the # sign, and be typed in all caps. The API request is sent, which returns the clan's river race log. The log includes all the individual races and each members performance during those races. The data returned on each individual player is their fame and repair points, ordered from lowest fame to highest fame.
