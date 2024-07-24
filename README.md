# Courtside Analytics

## Problem
The NBA is a data-driven game. The statistics of teams and players can be utilized to make informed conclusions about the team or player. Let’s say you wanted to figure out how Anthony Edwards impacts the Timberwolves. You may start with checking the difference in points per game for games where Anthony Edwards played and games where he didn’t. You may use something like Statmuse and retrieve the points per game for each class. Then, you would find the difference in the 2 values. You may then move on to checking the difference in other statistics. As you can see, this process can become quite lengthy especially if you want to analyze complex statistics and ask complex questions. Wouldn’t it be easier to just ask a system your question and instantly get the answer without performing any searches or any math on your end? 

Introducing Courtside Analytics, an AI powered platform that enables users to quickly get answers to their queries regarding NBA statistics. Using ReAct prompting, Courtside Analytics is able to understand your complex queries and generate an accurate answer quickly!
## Demo

## How to use Courtside Analytics

## System Design

``````mermaid
graph LR
    Query[Query]
    Output[Output]
    
    subgraph Agent[Agent]
        Prompt[Prompt]
        LLM[LLM]
        Tools
        Prompt --> LLM
        LLM <--> Tools
    end
    
    subgraph Tools
        Statmuse[Statmuse]
        Calculator[Calculator]
    end
    
    Tools <--> Environment[Environment]

    Query --> Prompt
    LLM --> Output

    classDef default fill:#000000,stroke:#4a4a4a,stroke-width:1px,color:#e0e0e0;
    classDef agent fill:#000033,stroke:#4a4a4a,stroke-width:1px,color:#e0e0e0;
    classDef tools fill:#000066,stroke:#4a4a4a,stroke-width:1px,color:#e0e0e0;
    class Agent agent;
    class Tools tools;
    
    style Query fill:#000033,stroke:#4a4a4a,stroke-width:1px,color:#e0e0e0;
    style Output fill:#000033,stroke:#4a4a4a,stroke-width:1px,color:#e0e0e0;
    style LLM fill:#003300,stroke:#4a4a4a,stroke-width:1px,color:#e0e0e0;
    style Environment fill:#330033,stroke:#4a4a4a,stroke-width:1px,color:#e0e0e0;

    linkStyle default stroke:#4a4a4a,stroke-width:2px;
    linkStyle 1 stroke:#4a4a4a,stroke-width:2px,fill:none,curve:curveBack;
    linkStyle 2 stroke:#4a4a4a,stroke-width:2px,fill:none,curve:curveBack;
