import plotly.graph_objects as go
import numpy as np

# Define the 15 steps and their categories
steps = [
    "Requirement & Planning",
    "Environment Setup", 
    "Data Acquisition Module",
    "Data Processing & Storage",
    "Technical Indicators Module",
    "Multi-Timeframe Analysis Engine",
    "Support/Resistance Detection",
    "Trendline Average Calculation",
    "Signal Generation Module",
    "Chart Visualization (UI)",
    "Real-time Data Handler",
    "Event-Driven Architecture", 
    "Risk Management Module",
    "Testing & Quality Assurance",
    "Deployment & Monitoring"
]

# Define categories and colors
categories = [
    "Planning", "Development", "Development", "Development", "Development",
    "Development", "Development", "Development", "Development", "Development",
    "Development", "Development", "Development", "Testing", "Deployment"
]

# Color mapping using brand colors
color_map = {
    "Planning": "#1FB8CD",      # Strong cyan
    "Development": "#2E8B57",   # Sea green  
    "Testing": "#D2BA4C",       # Moderate yellow
    "Deployment": "#DB4545"     # Bright red
}

# Create a more spread out layout - arrange in multiple rows/columns
# Arrange in 3 rows to better utilize space
positions = [
    (1, 3), (3, 3), (5, 3), (7, 3), (9, 3),     # Row 1: steps 1-5
    (1, 2), (3, 2), (5, 2), (7, 2), (9, 2),     # Row 2: steps 6-10
    (1, 1), (3, 1), (5, 1), (7, 1), (9, 1)      # Row 3: steps 11-15
]

# Create path connections for the flow
edge_paths = [
    # Row 1 connections (1->2->3->4->5)
    [(1,3), (3,3)], [(3,3), (5,3)], [(5,3), (7,3)], [(7,3), (9,3)],
    # Drop down from step 5 to step 6
    [(9,3), (9,2.5), (1,2.5), (1,2)],
    # Row 2 connections (6->7->8->9->10)
    [(1,2), (3,2)], [(3,2), (5,2)], [(5,2), (7,2)], [(7,2), (9,2)],
    # Drop down from step 10 to step 11
    [(9,2), (9,1.5), (1,1.5), (1,1)],
    # Row 3 connections (11->12->13->14->15)
    [(1,1), (3,1)], [(3,1), (5,1)], [(5,1), (7,1)], [(7,1), (9,1)]
]

# Create the figure
fig = go.Figure()

# Add connecting lines
for path in edge_paths:
    if len(path) == 2:  # Simple straight line
        x_coords = [path[0][0], path[1][0]]
        y_coords = [path[0][1], path[1][1]]
    else:  # Multi-point path
        x_coords = [point[0] for point in path]
        y_coords = [point[1] for point in path]
    
    fig.add_trace(go.Scatter(
        x=x_coords, y=y_coords,
        mode='lines',
        line=dict(width=3, color='#666666'),
        showlegend=False,
        hoverinfo='none'
    ))

# Add nodes for each category
for category in ["Planning", "Development", "Testing", "Deployment"]:
    cat_steps = []
    cat_positions = []
    cat_numbers = []
    
    for i, cat in enumerate(categories):
        if cat == category:
            cat_steps.append(steps[i])
            cat_positions.append(positions[i])
            cat_numbers.append(i+1)
    
    x_coords = [pos[0] for pos in cat_positions]
    y_coords = [pos[1] for pos in cat_positions]
    
    # Create abbreviated names that fit in 15 chars
    abbreviated_steps = []
    for step in cat_steps:
        if len(step) <= 15:
            abbreviated_steps.append(step)
        else:
            # Smart abbreviation
            if "Module" in step:
                abbrev = step.replace(" Module", "")
            elif "Engine" in step:
                abbrev = step.replace(" Engine", "")
            elif "Architecture" in step:
                abbrev = step.replace("Architecture", "Arch")
            elif "Visualization" in step:
                abbrev = step.replace("Visualization", "Visual")
            elif "Quality Assurance" in step:
                abbrev = step.replace("Quality Assurance", "QA")
            elif "Multi-Timeframe" in step:
                abbrev = step.replace("Multi-Timeframe", "Multi-TF")
            elif "Support/Resistance" in step:
                abbrev = "Support/Resist"
            else:
                abbrev = step[:15]
            abbreviated_steps.append(abbrev)
    
    hover_text = [f"Step {num}: {step}" for num, step in zip(cat_numbers, cat_steps)]
    
    fig.add_trace(go.Scatter(
        x=x_coords, y=y_coords,
        mode='markers+text',
        marker=dict(
            size=80,
            color=color_map[category],
            line=dict(width=3, color='white')
        ),
        text=[str(num) for num in cat_numbers],
        textposition="middle center",
        textfont=dict(size=14, color='white', family="Arial Black"),
        name=category,
        hovertext=hover_text,
        hoverinfo='text',
        showlegend=True
    ))

# Add step labels below each node
for i, (step, pos) in enumerate(zip(steps, positions)):
    # Use abbreviated names for display
    if len(step) <= 15:
        display_name = step
    else:
        if "Module" in step:
            display_name = step.replace(" Module", "")
        elif "Engine" in step:
            display_name = step.replace(" Engine", "")
        elif "Architecture" in step:
            display_name = step.replace("Architecture", "Arch")
        elif "Visualization" in step:
            display_name = step.replace("Visualization", "Visual")
        elif "Quality Assurance" in step:
            display_name = step.replace("Quality Assurance", "QA")
        elif "Multi-Timeframe" in step:
            display_name = step.replace("Multi-Timeframe", "Multi-TF")
        elif "Support/Resistance" in step:
            display_name = "Support/Resist"
        else:
            display_name = step[:15]
    
    fig.add_annotation(
        x=pos[0],
        y=pos[1] - 0.35,
        text=display_name,
        showarrow=False,
        font=dict(size=11, color='black'),
        xanchor='center',
        yanchor='top'
    )

# Add arrows at key connection points
arrow_positions = [
    # End of each row
    ((7.7, 3), (9.3, 3)),     # 4->5
    ((9, 2.8), (9, 2.2)),     # 5->6 (down)
    ((7.7, 2), (9.3, 2)),     # 9->10
    ((9, 1.8), (9, 1.2)),     # 10->11 (down)
    ((7.7, 1), (9.3, 1))      # 14->15
]

for start, end in arrow_positions:
    fig.add_annotation(
        x=end[0], y=end[1],
        ax=start[0], ay=start[1],
        xref='x', yref='y',
        axref='x', ayref='y',
        arrowhead=3,
        arrowsize=1.5,
        arrowwidth=3,
        arrowcolor='#666666',
        showarrow=True,
        text=""
    )

# Update layout
fig.update_layout(
    title="TradingView Python Trading System",
    showlegend=True,
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5),
    xaxis=dict(
        showgrid=False,
        showticklabels=False,
        zeroline=False,
        range=[0, 10]
    ),
    yaxis=dict(
        showgrid=False,
        showticklabels=False,
        zeroline=False,
        range=[0.3, 3.7]
    ),
    plot_bgcolor='white',
    paper_bgcolor='white'
)

# Save as both PNG and SVG
fig.write_image("tradingview_flowchart.png")
fig.write_image("tradingview_flowchart.svg", format="svg")

print("Enhanced flowchart created successfully!")
print("Layout: 3 rows x 5 columns for better space utilization")
print("Node size increased and labels positioned closer to nodes")