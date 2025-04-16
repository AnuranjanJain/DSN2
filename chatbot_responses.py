"""
Health Assistant Chatbot Responses Module

This module contains all the responses for the health assistant chatbot,
organized into dictionaries and lists for different types of responses.
"""

# Exact question matching dictionary
QUESTION_ANSWERS = {
    "how can i lower my cholesterol naturally": 
        "To lower cholesterol naturally: eat heart-healthy foods like oats, fatty fish, nuts, and foods rich in soluble fiber. Exercise regularly (aim for 30 minutes daily), lose weight if needed, quit smoking, and reduce alcohol consumption. Consider plant sterols and fiber supplements under medical guidance.",
    
    "what exercises are best for heart health": 
        "The best exercises for heart health include: 1) Aerobic activities like walking, jogging, cycling, or swimming (150 minutes/week), 2) Interval training which alternates intense activity with recovery periods, 3) Strength training with weights or resistance bands (2-3 times weekly), and 4) Flexibility exercises. Always start gradually and consult a doctor if you have existing heart conditions.",
    
    "what does systolic and diastolic blood pressure mean": 
        "Blood pressure readings have two numbers: Systolic (the top number) measures the pressure in your arteries when your heart beats. Diastolic (the bottom number) measures the pressure in your arteries when your heart rests between beats. Normal blood pressure is below 120/80 mmHg. High blood pressure increases heart disease risk and often has no symptoms.",
    
    "what are the main risk factors for heart disease": 
        "Major heart disease risk factors include: age (45+ for men, 55+ for women), family history, high blood pressure, high cholesterol, smoking, diabetes, obesity, physical inactivity, unhealthy diet, excessive alcohol, and chronic stress. Some factors can't be changed, but many can be managed with lifestyle modifications and appropriate medical care.",
    
    "how does the framingham model work": 
        "The Framingham model is based on data from the Framingham Heart Study, which began in 1948. It uses multiple risk factors (age, gender, cholesterol, blood pressure, smoking status, etc.) to calculate your 10-year risk of developing coronary heart disease. Our implementation uses a Random Forest classifier to provide accurate risk predictions based on these factors.",
    
    "what is a normal cholesterol level": 
        "Normal cholesterol levels are: Total cholesterol below 200 mg/dL, LDL ('bad') cholesterol below 100 mg/dL, HDL ('good') cholesterol above 60 mg/dL, and triglycerides below 150 mg/dL. Higher levels may increase heart disease risk. Regular testing is recommended, especially after age 20.",
    
    "what is a healthy bmi": 
        "A healthy BMI (Body Mass Index) ranges from 18.5 to 24.9. Below 18.5 is considered underweight, 25-29.9 is overweight, and 30+ is obese. While BMI is a useful screening tool, it doesn't directly measure body fat or account for muscle mass, so it should be one of several health assessments used.",
    
    "how does diabetes affect heart health": 
        "Diabetes significantly increases heart disease risk by damaging blood vessels and promoting high blood pressure, high cholesterol, and inflammation. People with diabetes are 2-4 times more likely to develop heart disease. Managing blood sugar, blood pressure, cholesterol, and maintaining a healthy lifestyle are crucial for reducing this risk.",
    
    "what are signs of a heart attack": 
        "Heart attack warning signs include: chest pain/pressure/tightness (like a weight on your chest), pain radiating to arms/back/neck/jaw, shortness of breath, cold sweats, unusual fatigue, nausea/vomiting, and lightheadedness. Women may experience more subtle symptoms. If you suspect a heart attack, call emergency services immediately.",
    
    "how can i improve my heart health": 
        "To improve heart health: 1) Eat a balanced diet rich in fruits, vegetables, whole grains, and lean proteins, 2) Exercise regularly (150+ minutes weekly), 3) Maintain a healthy weight, 4) Don't smoke and limit alcohol, 5) Manage stress, 6) Control blood pressure, cholesterol, and blood sugar, 7) Get adequate sleep, and 8) Have regular check-ups."
}

# Pattern-based responses dictionary
PATTERN_RESPONSES = {
    r'cholesterol': 
        "To lower cholesterol naturally: eat heart-healthy foods (oats, fatty fish, nuts), exercise regularly, lose weight if needed, quit smoking, and reduce alcohol consumption. Consider plant sterols and fiber supplements under medical guidance.",
    
    r'exercise|workout': 
        "The best exercises for heart health include aerobic activities (walking, jogging, cycling, swimming), interval training, and strength training. Aim for at least 150 minutes of moderate activity per week, spread across most days.",
    
    r'blood pressure|hypertension': 
        "Blood pressure has two numbers: Systolic (top) measures pressure during heartbeats, while diastolic (bottom) measures pressure between beats. Normal is below 120/80 mmHg. High blood pressure increases heart disease risk and often has no symptoms.",
    
    r'diet|food|eat': 
        "A heart-healthy diet includes fruits, vegetables, whole grains, lean protein, fish rich in omega-3s, nuts, and healthy oils. Limit saturated fats, trans fats, sodium, added sugars, and processed foods. The Mediterranean and DASH diets are excellent for heart health.",
    
    r'bmi|weight|obesity': 
        "Maintaining a healthy weight is crucial for heart health. A BMI of 18.5-24.9 is considered healthy. Excess weight, especially around the abdomen, increases risk for heart disease by promoting high blood pressure, high cholesterol, and diabetes. Even modest weight loss (5-10%) can significantly improve heart health metrics.",
    
    r'diabetes|glucose|sugar': 
        "Diabetes is a major risk factor for heart disease. High blood sugar damages blood vessels and nerves that control your heart. People with diabetes should monitor blood sugar levels carefully, maintain a heart-healthy diet, exercise regularly, and work closely with healthcare providers to manage both conditions.",
    
    r'smoking|tobacco': 
        "Smoking is one of the most significant risk factors for heart disease. It damages blood vessels, reduces oxygen in blood, and increases blood pressure. Quitting smoking can reduce heart disease risk by 50% after one year and approach non-smoker levels after 15 years. It's never too late to quit.",
    
    r'stress|anxiety': 
        "Chronic stress contributes to heart disease by raising blood pressure and leading to unhealthy coping behaviors. Effective stress management techniques include regular exercise, adequate sleep, deep breathing, meditation, yoga, connecting with others, and limiting stressors when possible.",
    
    r'alcohol|drinking': 
        "The relationship between alcohol and heart health is complex. While moderate consumption (up to 1 drink daily for women, 2 for men) may offer some protection, excessive alcohol raises blood pressure, contributes to obesity, and increases risk of heart failure and stroke. If you don't drink, don't start for potential health benefits.",
    
    r'framingham|model|risk score': 
        "Our heart risk assessment uses a model based on the Framingham Heart Study, one of the longest-running cardiovascular research projects. This study identified key risk factors for heart disease, including age, gender, cholesterol levels, blood pressure, smoking status, and diabetes. Our model analyzes these factors to estimate your 10-year risk of developing heart disease.",
    
    r'heart(?: |-)attack|cardiac arrest': 
        "A heart attack occurs when blood flow to part of the heart is blocked, usually by a blood clot. Warning signs include chest pain/pressure, discomfort in arms/back/neck/jaw, shortness of breath, cold sweats, and fatigue. These symptoms may be less obvious in women. If you suspect a heart attack, call emergency services immediately—quick treatment is crucial.",
    
    r'stroke': 
        "Stroke occurs when blood flow to the brain is interrupted, either by a clot (ischemic) or bleeding (hemorrhagic). Remember FAST: Face drooping, Arm weakness, Speech difficulty, Time to call emergency services. Risk factors for stroke overlap with heart disease: high blood pressure, smoking, diabetes, high cholesterol, and physical inactivity.",
    
    r'salt|sodium': 
        "High sodium intake contributes to high blood pressure, a major risk factor for heart disease. The American Heart Association recommends no more than 2,300mg daily (about 1 teaspoon of salt), with an ideal limit of 1,500mg. Most sodium comes from processed foods, not salt added during cooking or at the table.",
    
    r'sleep|insomnia|rest': 
        "Quality sleep is essential for heart health. Chronic sleep deprivation increases risk for high blood pressure, obesity, diabetes, and inflammation. Adults should aim for 7-9 hours of sleep per night. Improve sleep by maintaining a regular schedule, creating a restful environment, limiting screen time before bed, and avoiding caffeine and alcohol close to bedtime.",
    
    r'supplement|vitamin': 
        "Some supplements that may support heart health include omega-3 fatty acids, coenzyme Q10, fiber supplements, and plant sterols. However, evidence varies, and supplements should not replace heart-healthy eating and lifestyle. Always consult with a healthcare provider before starting any supplement, especially if you take medications.",
    
    r'caffeine|coffee': 
        "Research suggests moderate coffee consumption (1-3 cups daily) may be associated with lower heart disease risk. However, excessive caffeine can raise blood pressure and heart rate temporarily. The effect varies between individuals. Those with heart rhythm problems or uncontrolled high blood pressure should consult their doctor about caffeine intake.",
    
    r'mediterranean diet': 
        "The Mediterranean diet is one of the most heart-healthy eating patterns, emphasizing: olive oil, fruits, vegetables, whole grains, fish, nuts, and moderate red wine. This diet is low in red meat, processed foods, and added sugars. Studies show it can reduce heart disease risk by about 30% when followed consistently.",
    
    r'dash diet': 
        "The DASH (Dietary Approaches to Stop Hypertension) diet was specifically designed to lower blood pressure. It emphasizes fruits, vegetables, whole grains, lean proteins, and low-fat dairy while limiting sodium, added sugars, and saturated fats. This eating pattern can lower blood pressure in as little as two weeks when followed consistently.",
    
    r'heart.*(disease|attack|risk)': 
        "Major heart disease risk factors include high blood pressure, high cholesterol, smoking, diabetes, obesity, physical inactivity, and family history. Signs of heart attack may include chest pain/pressure, shortness of breath, and pain radiating to the arm, jaw, or back. If you suspect a heart attack, seek emergency help immediately.",
    
    r'(hi|hello|hey)': 
        "Hello! I'm your Cardio Guide Health Assistant. I can help answer questions about heart health, risk factors, and lifestyle changes. How can I assist you today?",
    
    r'(thank you|thanks)': 
        "You're welcome! Feel free to ask any other questions about heart health. I'm here to help.",
    
    r'heart.*(health|lifestyle)': 
        "A heart-healthy lifestyle includes: 1) Regular physical activity (150+ minutes weekly), 2) Balanced diet rich in fruits, vegetables, whole grains, and lean proteins, 3) Limited sodium, saturated fat, and added sugars, 4) No smoking, 5) Limited alcohol, 6) Healthy weight maintenance, 7) Stress management, and 8) Regular health checkups."
}

# Additional health topics
PATTERN_RESPONSES.update({
    r'cholesterol.*target': 
        "Target cholesterol levels are: Total cholesterol below 200 mg/dL, LDL ('bad') cholesterol below 100 mg/dL (below 70 mg/dL for those at high risk), HDL ('good') cholesterol above 60 mg/dL, and triglycerides below 150 mg/dL.",
    
    r'statins': 
        "Statins are medications that reduce cholesterol production in the liver. They're commonly prescribed to lower LDL cholesterol and reduce heart disease risk. While generally safe and effective, possible side effects include muscle pain, liver damage, increased blood sugar, and memory problems. Always take statins as prescribed and report side effects to your doctor.",
    
    r'heart.*test|cardiac test': 
        "Common heart tests include: ECG/EKG (records electrical signals), echocardiogram (ultrasound of heart), stress test (heart function during exercise), cardiac CT/MRI (detailed images), and coronary angiogram (shows blockages). Regular blood pressure and cholesterol tests are also important screening tools.",
    
    r'hypertension.*treatment': 
        "Hypertension treatment may include lifestyle changes (reduced sodium, DASH diet, regular exercise, weight management, stress reduction), and medications (diuretics, ACE inhibitors, ARBs, calcium channel blockers, etc.). Treatment plans are individualized based on blood pressure levels, other health conditions, and response to therapy.",
    
    r'atrial fibrillation|afib': 
        "Atrial fibrillation is an irregular heart rhythm that can increase stroke risk. Symptoms may include palpitations, weakness, shortness of breath, and fatigue, though some people have no symptoms. Treatment may include medications to control heart rate/rhythm, blood thinners to prevent clots, and in some cases, procedures like cardioversion or ablation.",
    
    r'palpitations': 
        "Heart palpitations are feelings of having a fast-beating, fluttering or pounding heart. Most are harmless and triggered by stress, exercise, caffeine, or certain medications. However, persistent or severe palpitations, especially with dizziness or chest pain, should be evaluated by a doctor as they may indicate arrhythmias or other heart conditions.",
    
    r'heart failure': 
        "Heart failure doesn't mean the heart has stopped working, but that it can't pump efficiently. Symptoms include shortness of breath, fatigue, and fluid retention (swelling). It's usually managed with medications, lifestyle changes, and sometimes devices or surgery. Early diagnosis and treatment can improve quality of life and prognosis.",
    
    r'heart valve': 
        "Heart valves ensure blood flows in the correct direction through your heart. Valve problems include stenosis (narrowing) or regurgitation (leaking), which can strain the heart. Causes include age-related changes, infections, or congenital conditions. Treatment ranges from monitoring to medication to valve repair or replacement.",
    
    r'coronary artery disease|cad': 
        "Coronary artery disease occurs when plaque builds up in the arteries supplying the heart, limiting blood flow. This can cause angina (chest pain), shortness of breath, or heart attack. Treatment includes lifestyle changes, medications to manage symptoms and risk factors, and possibly procedures like angioplasty or bypass surgery.",
    
    r'cpr|cardiopulmonary resuscitation': 
        "CPR can save lives during cardiac arrest. The current recommendation for untrained rescuers is hands-only CPR: 1) Call emergency services, 2) Push hard and fast in the center of the chest at a rate of 100-120 compressions per minute. Formal training is recommended to learn proper technique including rescue breaths.",
    
    r'aed|defibrillator': 
        "An AED (Automated External Defibrillator) is a portable device that can shock the heart back into normal rhythm during cardiac arrest. They're designed for public use with voice prompts guiding users through the process. When used with CPR in the first few minutes of cardiac arrest, AEDs significantly increase survival chances.",
    
    r'aspirin.*heart': 
        "Low-dose aspirin can help prevent blood clots in people at high risk of heart disease. However, current guidelines no longer recommend aspirin therapy for everyone. The benefits must be weighed against bleeding risks for each individual. Always consult your doctor before starting or stopping aspirin therapy.",
    
    r'antioxidant': 
        "Antioxidants help protect cells from damage caused by free radicals, which may contribute to heart disease. Foods rich in antioxidants include colorful fruits and vegetables, nuts, whole grains, and green tea. While a diet rich in these foods is beneficial, antioxidant supplements haven't shown the same heart benefits in research.",
    
    r'omega-?3': 
        "Omega-3 fatty acids may benefit heart health by reducing inflammation, lowering triglycerides, and slightly reducing blood pressure. Good sources include fatty fish (salmon, mackerel, sardines), walnuts, flaxseeds, and chia seeds. The American Heart Association recommends eating fish twice weekly. Supplements may be beneficial for some people under medical supervision.",
    
    r'genetic.*heart disease': 
        "Genetics play a role in heart disease risk. Family history of early heart disease (before 55 in men, 65 in women) increases your risk. While you can't change your genes, knowing your family history allows for earlier screening and more aggressive management of other risk factors you can control.",
    
    r'stress.*heart': 
        "Chronic stress contributes to heart disease risk through several mechanisms: raising blood pressure, promoting inflammation, and leading to unhealthy behaviors like overeating or substance use. Effective stress management through regular exercise, adequate sleep, relaxation techniques, and social connections can help protect your heart.",
    
    r'vegetarian.*heart|vegan.*heart': 
        "Well-planned vegetarian and vegan diets can be heart-healthy, as they're typically high in fiber and antioxidants while low in saturated fat. Studies show vegetarians often have lower rates of heart disease. Key nutrients to focus on include protein, omega-3s, vitamin B12, iron, zinc, and calcium, which may require careful food selection or supplementation.",
    
    r'water.*heart': 
        "Staying properly hydrated supports heart health by helping your heart pump blood more easily. Dehydration can strain the heart and trigger abnormal heart rhythms. The amount of water needed varies by individual, but a common recommendation is about 8 cups (64 ounces) daily, with more needed during hot weather or exercise.",

    r'target heart rate': 
        "Your target heart rate during exercise depends on your age and fitness goals. A general formula is 220 minus your age, then take 50-85% of that number for moderate to vigorous intensity. For example, a 40-year-old would have a maximum heart rate of 180 and a target range of 90-153 beats per minute. Heart rate monitors can help you track this during workouts.",
        
    r'ecg|ekg|electrocardiogram': 
        "An ECG or EKG (electrocardiogram) records the electrical signals in your heart through electrodes placed on your skin. It can detect abnormal heart rhythms, evidence of heart attacks (past or in progress), and structural issues affecting electrical signaling. It's a quick, painless test that provides valuable information about heart function.",
    
    r'longevity.*heart|lifespan.*heart': 
        "Heart health is closely tied to longevity. Research shows that controlling these seven factors can add years to your life: managing blood pressure, controlling cholesterol, reducing blood sugar, getting active, eating better, losing weight, and stopping smoking. People who optimize these factors may live 10+ years longer than those who don't."
})

# Random health tips for tip requests
HEALTH_TIPS = [
    "Try to stand up and move for at least 5 minutes every hour if you have a sedentary job.",
    
    "Laughter is good medicine for your heart! Regular laughter may lower stress hormones and inflammation in your body.",
    
    "Dark chocolate (70%+ cocoa content) contains flavonoids that may help reduce blood pressure and improve heart health when consumed in moderation.",
    
    "Consider the DASH diet: rich in fruits, vegetables, whole grains, and low-fat dairy while limiting sodium—it's scientifically proven to lower blood pressure.",
    
    "A handful of nuts (about 1.5 ounces) daily may reduce your risk of cardiovascular disease by up to 30%, according to multiple studies.",
    
    "Try adding mindfulness meditation to your daily routine. Even 10 minutes can help lower stress levels and blood pressure.",
    
    "Make half your plate vegetables at lunch and dinner to easily increase your fiber intake and support heart health.",
    
    "Sleep 7-9 hours nightly. Poor sleep quality is linked to higher blood pressure and increased risk of heart disease.",
    
    "Add strength training to your exercise routine 2-3 times weekly. Building muscle improves how your body processes cholesterol.",
    
    "Track your heart rate during exercise: A good target is 50-85% of your maximum heart rate (220 minus your age).",
    
    "Consider keeping a food journal for a week to identify areas where you can improve your heart-healthy eating habits.",
    
    "Stay hydrated! Proper hydration helps your heart pump blood more efficiently through your body.",
    
    "Replace refined grains with whole grains like brown rice, whole wheat bread, and oatmeal to reduce heart disease risk.",
    
    "Try the Mediterranean diet, which emphasizes olive oil, fish, nuts, fruits, and vegetables—it's associated with a 30% lower risk of cardiovascular events.",
    
    "Aim for 30 minutes of moderate exercise 5 days a week, or 25 minutes of vigorous exercise 3 days a week, plus two days of strength training.",
    
    "Monitor your waist circumference: Risk increases with measurements over 40 inches (102 cm) for men or 35 inches (88 cm) for women.",
    
    "Swap saturated fats (butter, full-fat dairy) for unsaturated options (olive oil, avocados) to improve your cholesterol profile.",
    
    "Try interval training: Alternating between high and moderate intensity during exercise can improve heart health more efficiently than steady-state exercise alone.",
    
    "Increase your omega-3 intake by having fatty fish like salmon, mackerel, or sardines twice a week.",
    
    "Practice gratitude daily: Research shows that positive emotions are associated with lower risk of heart disease.",
    
    "Add plant-based proteins like beans, lentils, and tofu to your diet several times a week to reduce saturated fat intake.",
    
    "Monitor your blood pressure at home between doctor visits, especially if you have hypertension. Keep a log to share with your healthcare provider."
]

# Default response when no pattern matches
DEFAULT_RESPONSE = "I'm your heart health assistant. I can answer questions about heart disease, cholesterol, blood pressure, exercise, and heart-healthy diets. How can I help you with your cardiovascular health today?" 