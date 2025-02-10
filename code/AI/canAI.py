import torch  
import torch.nn as nn  
import numpy as np  

class CAN_LSTM(nn.Module):  
    def __init__(self, input_size, hidden_size, num_layers, output_size):  
        super(CAN_LSTM, self).__init__()  
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)  
        self.fc = nn.Linear(hidden_size, output_size)  

    def forward(self, x):  
        out, _ = self.lstm(x)  
        out = self.fc(out[:, -1, :])  # Take the last output  
        return out  

# Example: Train with CAN data converted into sequences
