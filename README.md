![Water quality](https://cdn-icons-png.flaticon.com/512/11707/11707251.png)

Accra, Ghana’s vibrant capital and a fast-growing city. Water is life, but supplying safe drinking water is becoming more difficult as raw water sources face increasing pressure from pollution, mining activities, and changing environmental conditions.

In this project, you will support the Odaso Water Treatment Plant by analyzing raw water quality data from the Oda River. The goal is to identify patterns in turbidity, pH, temperature, and alkalinity, then build a predictive model that can help determine the optimal coagulant dosage for more efficient and cost-effective treatment.

This matters because coagulation-flocculation is one of the most important steps in water treatment, and getting the dosage right can improve turbidity removal, reduce chemical waste, and help ensure safe water for surrounding communities.

## The Data

You have been provided with a single dataset for this study. A brief summary of the key variables is shown below.

# water_quality.csv

| Column | Description |
|--------|-------------|
| `Date` | The date the the reading was taken. |
| `Year` | The year of sampling. |
| `Month` | The month the the reading was taken. |
| `pH` | Indicates how acidic or alkaline the water is. |
| `Turbidity` | Measures how cloudy the raw water is. Higher values usually indicate more suspended particles (NTU). |
| `Conductivity` | Measures  how conductive the water is (µS/cm). |
| `Temperature` | The raw water temperature at the time of sampling (°C). |
| `Coagulant_Dosage` | The amount of coagulant used or determined to be optimal during jar tests (kg/day). |