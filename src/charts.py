import plotly.express as px
import plotly.graph_objects as go


# Fraud vs Legitimate Pie Chart
def fraud_pie_chart(fraud_count, legit_count):

    fig = px.pie(
        names=["Fraud", "Legitimate"],
        values=[fraud_count, legit_count],
        title="Fraud vs Legitimate Transactions"
    )

    return fig


# Fraud Probability Gauge Chart
def probability_gauge(probability):

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=probability * 100,

        title={'text': "Fraud Risk Score"},

        gauge={
            'axis': {'range': [0, 100]},

            'bar': {'color': "red"},

            'steps': [
                {'range': [0, 30], 'color': "green"},
                {'range': [30, 70], 'color': "orange"},
                {'range': [70, 100], 'color': "red"}
            ]
        }
    ))

    return fig