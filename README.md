# Courtside Analytics
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://courtside-analytics.streamlit.app/)

## Problem
The NBA is a data-driven game. The statistics of teams and players can be utilized to make informed conclusions about the team or player. Let’s say you wanted to figure out how Anthony Edwards impacts the Timberwolves. You may start with checking the difference in points per game for games where Anthony Edwards played and games where he didn’t. You may use something like Statmuse and retrieve the points per game for each class. Then, you would find the difference in the 2 values. You may then move on to checking the difference in other statistics. As you can see, this process can become quite lengthy especially if you want to analyze complex statistics and ask complex questions. Wouldn’t it be easier to just ask a system your question and instantly get the answer without performing any searches or any math on your end? 

Introducing Courtside Analytics, an AI powered platform that enables users to quickly get answers to their queries regarding NBA statistics. Using ReAct prompting, Courtside Analytics is able to understand your complex queries and generate an accurate answer quickly!

## Demo

https://github.com/user-attachments/assets/79a0f823-eec6-48d9-97ab-6735bbf26ee5

## How to use Courtside Analytics
If you just want to use Courtside Analytics, you can navigate to the [webpage](https://courtside-analytics.streamlit.app/).

If you would like to work with the tool in a development setting, please follow the following procedure:
1. Clone the repository. I highly recommend having a virtual environment for the project; however, that is not necessary.
2. Navigate to the project folder and install dependencies: 
```
poetry install
```
3. Finally, you can navigate to the "src" folder and run the app:
```
poetry run streamlit run app.py
```

## System Design
``````mermaid
graph TD
    A[User]
    B[Streamlit Web UI]
    C[GPT 4.0]
    F[Answer]
    
    A -->|Query| B
    B -->|Query| Agent
    B -->|Answer| A
    
    subgraph Agent
        C
        subgraph Tools
            D[Calculator]
            E[Statmuse]
            G[DuckDuckGo Search]
        end
    end
    
    Agent --> F
    F --> B
    
    linkStyle default stroke:#FFFFFF
``````
## Author's Note

Note, since Courtside Analytics is a platform that utilizes large language models (LLMs), it is important to be aware of the following:
1. LLMs hallunicate. What this means is that they may provide false information. While having access to tools lowers this risk, it doesn't completely mitigate it. Whenever you use Courtside Analytics, you should be aware of this fact.
