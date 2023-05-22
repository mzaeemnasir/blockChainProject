import React, { useState } from 'react';
import backgroundImage from './image/q.jpg';

function CustomIndicator() {
  const [conditions, setConditions] = useState([{ indicator: '', length: '', condition: '', value: '' }]);
  const [takeProfit, setTakeProfit] = useState(false);
  const [stopLoss, setStopLoss] = useState(false);

  const indicators = ['PriceOpen', 'PriceHigh', 'PriceLow', 'PriceClose', "MACD 12,26", "EMA", "SMA", "RSI"];
  const conditionsList = ['Greater Than Or Equal', 'Less Than Or Equal', 'Crosses Above', 'Crosses Below', 'Equal'];
  const choice = ["Indicator", "ConstantValue"]


  const handleAddCondition = () => {
    setConditions([...conditions, { indicator: '', length: '', condition: '', value: '', valueLength: '' }]);
  };

  const handleRemoveCondition = (index) => {
    const newConditions = [...conditions];
    newConditions.splice(index, 1);
    setConditions(newConditions);
  };

  const handleConditionChange = (index, event) => {
    const { name, value } = event.target;
    const newConditions = [...conditions];
    newConditions[index] = {
      ...newConditions[index],
      [name]: value,
    };
    setConditions(newConditions);
  };

  const handleTakeProfitChange = (event) => {
    setTakeProfit(event.target.checked);
  };

  const handleStopLossChange = (event) => {
    setStopLoss(event.target.checked);
  };

  const handleSubmit = () => {
    const data = {
      conditions,
      takeProfit,
      stopLoss,
    };
    const jsonData = JSON.stringify(data);
    console.log(jsonData);
    alert('JSON data: ' + jsonData);

    // Clear input fields
    setConditions([{ indicator: '', length: '', condition: '', value: '' }]);
    setTakeProfit(false);
    setStopLoss(false);
  };

  return (
    <div
      style={{
        backgroundImage: `url(${backgroundImage})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        padding: '20px',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        minHeight: '100vh',
      }}
    >
      <h1 style={{ color: '#f5f5f5', marginBottom: '100px', marginTop: '200px' }}>Create your own Custom Trading Bot</h1>
      {conditions.map((condition, index) => (
        <div key={index}>
          <select
            name="indicator"
            value={condition.indicator}
            onChange={(event) => handleConditionChange(index, event)}
            style={{ backgroundColor: '#fff', padding: '5px', borderRadius: '3px', border: '1px solid #ccc', marginRight: '10px' }}
          >
            <option value="">Select Indicator</option>
            {indicators.map((indicator) => (
              <option value={indicator} key={indicator}>
                {indicator}
              </option>
            ))}
          </select>
          {condition.indicator.toString().startsWith("Price") === false && condition.indicator.toString().startsWith("MACD") === false ? (
            <input
              type="text"
              name="length"
              value={condition.length}
              onChange={(event) => handleConditionChange(index, event)}
              placeholder="Length"
              style={{ backgroundColor: '#fff', padding: '5px', borderRadius: '3px', border: '1px solid #ccc', marginRight: '10px' }}
            />
          ) : null}
          <select
            name="condition"
            value={condition.condition}
            onChange={(event) => handleConditionChange(index, event)}
            style={{ backgroundColor: '#fff', padding: '5px', borderRadius: '3px', border: '1px solid #ccc', marginRight: '10px' }}
          >
            <option value="">Select Condition</option>
            {conditionsList.map((condition) => (
              <option value={condition} key={condition}>
                {condition}
              </option>
            ))}
          </select>
          <select
            name="choice"
            value={condition.choice}
            onChange={(event) => handleConditionChange(index, event)}
            style={{ backgroundColor: '#fff', padding: '5px', borderRadius: '3px', border: '1px solid #ccc', marginRight: '10px' }}
          >
            <option value="">Select Choice</option>
            {choice.map((choice) => (
              <option value={choice} key={choice}>
                {choice}
              </option>
            ))}
          </select>
          {condition.choice === "ConstantValue" ? (
            <input
              type="text"
              name="value"
              value={condition.value}
              onChange={(event) => handleConditionChange(index, event)}
              placeholder="Value"
              style={{ backgroundColor: '#fff', padding: '5px', borderRadius: '3px', border: '1px solid #ccc', marginRight: '10px' }}
            />
          ) : null}

          {condition.choice === "Indicator" ? (
            <select
              name="value"
              value={condition.value}
              onChange={(event) => handleConditionChange(index, event)}
              style={{ backgroundColor: '#fff', padding: '5px', borderRadius: '3px', border: '1px solid #ccc', marginRight: '10px' }}
            >
              <option value="">Select Indicator</option>
              {indicators.map((indicator) => (
                <option value={indicator} key={indicator}>
                  {indicator}
                </option>
              ))}
            </select>



          ) : null}
          {condition.value.toString().startsWith("Price") === false && condition.value.toString().startsWith("MACD") === false ? (
            <input
              type="text"
              name="valueLength"
              value={condition.valueLength}
              onChange={(event) => handleConditionChange(index, event)}
              placeholder="Length"
              style={{ backgroundColor: '#fff', padding: '5px', borderRadius: '3px', border: '1px solid #ccc', marginRight: '10px' }}
            />
          ) : null}





          {conditions.length > 1 ? (
            <button onClick={() => handleRemoveCondition(index)} style={{ backgroundColor: 'blue', color: '#fff', border: 'none', padding: '5px 10px', borderRadius: '3px', marginRight: '10px' }}>
              x
            </button>
          ) : null}
        </div>
      ))}
      <button onClick={handleAddCondition} style={{ margin: '20px', backgroundColor: 'blue', color: '#fff', border: 'none', padding: '10px 20px', borderRadius: '3px', marginBottom: '10px' }}>
        Add Condition
      </button>
      <div>
        <label style={{ color: '#ffffff', margin: '10px' }}>
          <input
            type="checkbox"
            checked={takeProfit}
            onChange={handleTakeProfitChange}
          />
          Take Profit
        </label>
        {takeProfit ? (
          <input
            type="text"
            placeholder="Exit if user gained X%"
            style={{
              backgroundColor: '#ffffff',
              padding: '5px',
              borderRadius: '3px',
              border: '1px solid #ccc',
              marginLeft: '10px',
            }}
          />
        ) : null}
      </div>
      <div>
        <label style={{ color: '#ffffff', margin: '13px' }}>
          <input
            type="checkbox"
            checked={stopLoss}
            onChange={handleStopLossChange}
          />
          Stop Loss
        </label>
        {stopLoss ? (
          <input
            type="text"
            placeholder="Exit if loss more than X%"
            style={{ backgroundColor: '#ffffff', padding: '5px', borderRadius: '3px', border: '1px solid #ccc', marginLeft: '10px' }}
          />
        ) : null}
      </div>
      <button onClick={handleSubmit} style={{ backgroundColor: 'blue', color: '#fff', border: 'none', padding: '10px 20px', marginTop: '30px', borderRadius: '3px' }}>
        Submit
      </button>
    </div >
  );
}

export default CustomIndicator;
