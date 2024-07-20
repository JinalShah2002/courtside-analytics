# Courtside Analytics

## Problem
Imagine you are someone who works with NBA statistics. You want to identify how a player’s performance has changed over the years (i.e by how much has Anthony Edwards’s points per game changed from last season to this season). The current process for this is to perform a Google search and navigate yourself to a statistics website (i.e ESPN or StatMuse). After navigating to said website(s), you would first find the required statistics and perform a calculation to answer your query. This process can be long and arduous, especially if you are asking complex queries. In comes Courtside Analytics: an AI tool that enables you to dive deeper into NBA statistics via language. Using ReAct prompting, Courtside Analytics is able to process complex questions and provide accurate answers. All you need to do is ask!

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
