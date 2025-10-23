import plotly.graph_objects as go

# Create a layered architecture diagram using Plotly
fig = go.Figure()

# Define layer positions and colors (using the brand colors from theme)
layer_colors = ['#1FB8CD', '#DB4545', '#2E8B57', '#5D878F']
layer_names = ['Presentation Layer', 'Business Logic Layer', 'Data Layer', 'Infrastructure Layer']

# Original component names from instructions
layer_components = [
    ['Chart Visualization', 'User Interface', 'Event Markers'],
    ['Multi-Timeframe Analysis Engine', 'Technical Indicators Calculator', 'Support/Resistance Detector', 'Signal Generation Module', 'Risk Management Module'],
    ['Data Acquisition Module', 'Data Storage', 'Real-time Data Handler'],
    ['Event-Driven Architecture', 'Logging & Monitoring', 'Deployment']
]

# Abbreviated versions for display (keeping under 15 chars as per instructions)
layer_components_short = [
    ['Chart Visual', 'User Interface', 'Event Markers'],
    ['Multi-Frame', 'Tech Indicators', 'Support/Resist', 'Signal Gen', 'Risk Mgmt'],
    ['Data Acquire', 'Data Storage', 'Real-time'],
    ['Event-Driven', 'Log & Monitor', 'Deployment']
]

# Draw layers as rectangles with better spacing
y_positions = [3.2, 2.4, 1.6, 0.8]
layer_height = 0.6
layer_width = 10

for i, (layer_name, components, y_pos, color) in enumerate(zip(layer_names, layer_components_short, y_positions, layer_colors)):
    # Draw layer background
    fig.add_shape(
        type="rect",
        x0=1, y0=y_pos - layer_height/2,
        x1=layer_width + 1, y1=y_pos + layer_height/2,
        fillcolor=color,
        opacity=0.2,
        line=dict(color=color, width=2)
    )
    
    # Add layer title (horizontal, better positioned)
    fig.add_annotation(
        x=0.5, y=y_pos,
        text=f"<b>{layer_name}</b>",
        showarrow=False,
        font=dict(size=11, color="black"),
        textangle=0,
        xanchor="right",
        yanchor="middle"
    )
    
    # Add components as boxes within each layer
    comp_width = (layer_width - 0.5) / len(components)
    for j, component in enumerate(components):
        x_pos = 1.25 + j * comp_width + comp_width/2
        
        # Component box - larger to fit text better
        fig.add_shape(
            type="rect",
            x0=1.25 + j * comp_width, y0=y_pos - 0.22,
            x1=1.25 + (j + 1) * comp_width - 0.05, y1=y_pos + 0.22,
            fillcolor='white',
            opacity=0.95,
            line=dict(color=color, width=1.5)
        )
        
        # Component text - better sized
        fig.add_annotation(
            x=x_pos, y=y_pos,
            text=component,
            showarrow=False,
            font=dict(size=9, color="black"),
            xanchor="center",
            yanchor="middle"
        )

# Add clearer communication arrows between layers
arrow_x = layer_width + 2

# Downward arrows with labels
communication_down = ['User Events', 'Data Requests', 'Infra Services']
for i in range(3):
    fig.add_annotation(
        x=arrow_x, y=y_positions[i] - 0.15,
        ax=arrow_x, ay=y_positions[i+1] + 0.15,
        arrowhead=3, arrowsize=1.5, arrowwidth=3, arrowcolor="#333333",
        text=communication_down[i], 
        showarrow=True,
        font=dict(size=8, color="#333333"),
        textangle=0,
        xanchor="center"
    )

# Upward arrows with labels  
communication_up = ['Display Updates', 'Processed Data', 'System Resources']
for i in range(3):
    fig.add_annotation(
        x=arrow_x + 1.2, y=y_positions[i+1] + 0.15,
        ax=arrow_x + 1.2, ay=y_positions[i] - 0.15,
        arrowhead=3, arrowsize=1.5, arrowwidth=3, arrowcolor="#666666",
        text=communication_up[i],
        showarrow=True,
        font=dict(size=8, color="#666666"),
        textangle=0,
        xanchor="center"
    )

# Update layout with better spacing
fig.update_layout(
    title="TradingView 4-Layer Architecture",
    showlegend=False,
    xaxis=dict(visible=False, range=[0, 15]),
    yaxis=dict(visible=False, range=[0.3, 3.7]),
    plot_bgcolor='white',
    paper_bgcolor='white'
)

# Save the chart
fig.write_image("tradingview_architecture.png")
fig.write_image("tradingview_architecture.svg", format="svg")

print("Updated architecture diagram saved successfully!")