12-Week Python Plan for a Web3 Dev with a Mining Background
Oct 16, 2026 · @kenny
How to use this plan
Budget 8–10 hours a week: about 1 hour on weekdays and a longer session on the weekend. Because you already write JavaScript and Solidity, you can skip the "what is a variable" material and focus on Python's way of doing things.
Set up once (Week 1, day 1):
• Install Python 3.12+ from python.org (tick "Add to PATH" on Windows)
• Use VS Code with the Python extension, the same editor you likely use for web3
• Learn to make a virtual environment: python -m venv .venv, then pip install packages inside it (like npm install in a project folder)
• Create a GitHub repo called python-mining-journey and commit every exercise. This becomes your portfolio.
Use AI as your tutor, not your typist. Write the code yourself first. Then ask AI to review it, explain errors, or show how it would look in JavaScript so you can map the concepts. If you only copy AI output, you won't actually learn.
Each week has three parts: concepts to learn, a JavaScript comparison to anchor them, and a mining-flavored exercise that keeps your engineering knowledge in play.
Phase 1 (Weeks 1–3): Python fundamentals
Goal: write clean Python scripts as comfortably as you write JavaScript.
Week 1: Syntax and core types
Learn: variables, strings and f-strings, numbers, lists, dicts, tuples, if/elif/else, for and while loops, indentation instead of braces.
JS comparison: list ≈ array, dict ≈ object, print() ≈ console.log(), for ore in ores: ≈ for (const ore of ores), None ≈ null, True/False are capitalized.
Exercise: a grade calculator. Store 10 drillhole samples as a list of dicts ({"hole": "DH-01", "depth_m": 45, "cu_pct": 0.82}). Print each sample's grade, flag anything above a cut-off grade of 0.5% Cu, and compute the average grade.
Week 2: Functions, modules and errors
Learn: functions with default and keyword arguments, return, list and dict comprehensions, import, splitting code across files, try/except.
JS comparison: def ≈ function, lambda ≈ arrow function (but limited to one expression), comprehensions replace many .map() and .filter() chains, try/except ≈ try/catch.
Exercise: a mining calculations module (mining_calcs.py) with functions for tonnage (volume × density), contained metal (tonnage × grade), stripping ratio (waste ÷ ore), and head grade after dilution. Import it into a second script and handle bad inputs like negative volumes.
Week 3: Files, classes and the command line
Learn: reading and writing text and CSV files with with open(...), the csv and json modules, classes and __init__, argparse for command-line tools.
JS comparison: classes look familiar but use explicit self instead of this; JSON handling via json.load() ≈ JSON.parse().
Exercise: a Deposit class with name, mineral, tonnage and grade, and a method that returns contained metal and estimated in-situ value at a given price. Load 5 deposits from a CSV file and write a summary report to JSON. Run it from the terminal with the price as an argument.
Phase 2 (Weeks 4–6): Working with data
Goal: load messy real-world data, clean it, analyze it and chart it. This is the skill most employers actually pay for.
Week 4: pandas basics
Learn: Jupyter notebooks, pandas DataFrames, reading CSV and Excel files, selecting columns, filtering rows, sorting, groupby, handling missing values.
Exercise: download a public dataset of mineral production by country (USGS Mineral Commodity Summaries publishes these). Find the top 10 producers of lithium, cobalt and copper, and calculate each country's share of world output.
Week 5: Charts with matplotlib
Learn: line, bar and scatter charts, labels and titles, saving charts as images. Optionally try plotly for interactive charts.
Exercise: chart 10+ years of copper and lithium prices. Add a second chart of your Week 4 production shares. Write three sentences under each chart saying what it shows. Interpreting charts is as valuable as making them.
Week 6: APIs and automation
Learn: the requests library, reading JSON from APIs, API keys stored in a .env file (never in code), scheduling a script to run daily.
JS comparison: requests.get(url).json() ≈ await fetch(url).then(r => r.json()), but synchronous by default.
Exercise: build a commodity price tracker. Pull daily metal prices from a free API, save them to a CSV, and print an alert when a price moves more than 3% in a day. Bonus: pull crypto prices too, since you know that world, and compare volatility.
Phase 2 milestone: publish one clean notebook on GitHub titled something like "Critical minerals: who produces what" with charts and short commentary. Share it on LinkedIn.
Phase 3 (Weeks 7–9): Mining engineering with Python
Goal: turn your degree into a technical edge. Most Python developers can't do this part; most mining engineers can't code it.
Week 7: Geospatial data
Learn: coordinates and projections, geopandas, shapefiles and GeoJSON, plotting points on maps with folium.
Exercise: map mineral occurrences or mining licences in a region you care about. Many geological surveys publish this data; for Nigeria, the Nigerian Geological Survey Agency and the Mining Cadastre Office are starting points, and global datasets like USGS mineral resource data work too. Color points by mineral type and add a popup with details for each site.
Week 8: Drillhole and grade analysis
Learn: numpy for fast math, basic statistics (mean, variance, histograms), compositing samples by length, simple interpolation.
Exercise: using a public or synthetic drillhole dataset, composite samples to fixed intervals, plot grade histograms, and estimate grades between holes with inverse distance weighting (IDW). Compare your estimate against your own hand calculation for one block. Ask AI to explain kriging conceptually; you don't need to implement it yet.
Week 9: Mine economics model
Learn: structuring a calculation model in code, functions that take scenarios, sensitivity analysis.
Exercise: build a simple cash-flow model for a small mine: annual tonnage, grade, recovery, metal price, operating cost and capital cost, producing NPV and payback period. Run it at five different metal prices and chart how NPV changes. This mirrors real feasibility work and shows employers you think like an engineer.
Phase 4 (Weeks 10–12): Capstone — mineral traceability on-chain
Goal: one project that combines all three of your skill sets and becomes the centerpiece of your portfolio.
Week 10: Python meets the blockchain
Learn: web3.py (Python's equivalent of ethers.js), connecting to a testnet RPC, reading contract state, sending transactions from Python, listening for events.
JS comparison: Web3(Web3.HTTPProvider(rpc_url)) ≈ new ethers.JsonRpcProvider(rpcUrl). Same concepts you already know, different syntax.
Exercise: write a Python script that reads balances and recent events from a contract you've already deployed, then sends a test transaction.
Week 11: Build the traceability system
Build:
1. A Solidity contract (your strength) that registers mineral batches with an ID, origin mine, weight, grade and a hash of the assay certificate, and records each custody transfer: mine → processor → exporter → buyer.
2. A Python backend that takes batch data from a CSV (simulating a mine's records), hashes the documents, and writes each step on-chain via web3.py.
3. A Python verification script: given a batch ID, it pulls the full history from the chain and checks the document hashes match.
Deploy on a testnet only. Never use real funds for a portfolio project.
Week 12: Dashboard, write-up and launch
Build: a simple dashboard with Streamlit (pure Python, no frontend code needed) showing batches on a map from Week 7, their custody history, and grade and weight data.
Write-up: a README explaining the problem (proving where critical minerals come from), how your system works, its honest limits (the chain can only verify what's entered; bad data in is still bad data), and what a real deployment would need.
Launch: post a short demo video and the write-up on LinkedIn and X. Tag it with critical minerals, supply chain and real-world assets topics. This is the project that starts conversations with employers.
Free resources and datasets
Resource
Use it for
Phase
Python official tutorial
Core syntax reference
1
Automate the Boring Stuff with Python
Practical scripting, files, automation
1–2
freeCodeCamp
Structured Python and data analysis courses
1–2
Kaggle Learn
Short pandas and data visualization courses
2
USGS Mineral Commodity Summaries
Production and reserves data by country
2–3
GeoPandas docs
Geospatial analysis
3
web3.py docs
Python blockchain interaction
4
Streamlit docs
Quick dashboards in pure Python
4
Links are from memory, not checked today; if one has moved, search the resource name.
Progress checklist
[ ] Week 1: Grade calculator for drillhole samples
[ ] Week 2: mining_calcs.py module with error handling
[ ] Week 3: Deposit class, CSV in, JSON report out
[ ] Week 4: Critical minerals production analysis in pandas
[ ] Week 5: Price and production charts with commentary
[ ] Week 6: Daily commodity price tracker with alerts
[ ] Phase 2 milestone: notebook published and shared on LinkedIn
[ ] Week 7: Interactive map of mineral sites
[ ] Week 8: Drillhole compositing and IDW grade estimate
[ ] Week 9: Mine cash-flow model with NPV sensitivity chart
[ ] Week 10: web3.py script reading and writing to a testnet contract
[ ] Week 11: Traceability contract, backend and verifier working end to end
[ ] Week 12: Streamlit dashboard, README and demo post published