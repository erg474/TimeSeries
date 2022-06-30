# Financial Time Series Analysis
Overview of Financial Time Series Analysis. With Stock Market and Machine Learning information being so readily available, 
the fact that there is not a consistent return for traders using it for trading should be noted. The stock market is a chaotic
system of order 2, so don't expect these algorithms to work automatically without thorough research into them.
In this repo I look into various methods for stock analysis and predictions, and find out whether these methods are viable.

Contents - A few Common Quantitative Methods for Financial Time Series Analysis are :
1. Random Forests
2. SVMs (Support-Vector Machines)
3. Neural Network Architectures
4. LSTM (Long Short Term Memory) (included in 3)
5. Reinforcement Learning

Other Useful Financial Investigations:
1. Discounted Cash Flow Models - Instrinsic Analysis
2. Fundamental Analysis
3. Technical Analysis on Random Walk Models, to test whether the Technical Analysis indicators are pseudoscientific


Details
1.
2.
3.

4. LSTMs - LSTMs are a type of neural network
A little more effort will be required to formulate the problem statement, inputs, and model. Some good direction to head in would be predicting changes in value (a derivative or second derivative) instead of the value itself. Predicting only the stock price movements (binary classification problem) could be another option. Or to use an ensemble of models to achieve combined/different goals. I’d recommend that you try to gain stronger domain knowledge in these fields first, followed by explorations — don’t restrict yourself to these ideas or other ideas you see on the internet.
-Good for low noise
For stock forecasting, you need to identify (and prove!) a signal that is (a) stable, not tied to a particular period of time; (b) has fluctuations that are large enough that the profit opportunity won't be lost in the bid-ask spread; and (c) has timing characteristics (frequency, warning time, etc.) that permit trading.
You need signal - LSTMs (and neural networks generally) are very good at automation aka making decisions from complex inputs with low noise.

The stock market is absolutely not one of these things, and you would need to find the right data representation to have a fighting chance. As a bonus, many emergent trends and periodicities disappear, since people try to act just before the trend - thereby destroying it.
The problem is that you're competing on a zero-sum basis against everyone else who is trying to predict the market, because the first hedge fund to spot a movement coming at some point in the future will trade in a way that makes the movement happen now. So the question is whether you're smarter and have more resources than the people who predict the market professionally, and the answer is no, you're not
Not impossible, but typical loss functions are derived assuming homoskedastic noise. This assumption is violated rather badly in many financial contexts.





Testing git again