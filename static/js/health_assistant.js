// AI Health Assistant - Client-side functionality
document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const assistantBtn = document.getElementById('health-assistant-btn');
    const assistantContainer = document.getElementById('health-assistant-container');
    const assistantClose = document.getElementById('health-assistant-close');
    const messageArea = document.getElementById('health-assistant-messages');
    const userInput = document.getElementById('health-assistant-input');
    const sendBtn = document.getElementById('health-assistant-send');

    // Initial greeting message
    const initialMessages = [
        {
            text: "Hello! I'm your Health Assistant. How can I help you today?",
            sender: 'bot'
        }
    ];

    // Open/Close assistant chat
    assistantBtn.addEventListener('click', function() {
        assistantContainer.classList.add('active');
    });

    assistantClose.addEventListener('click', function() {
        assistantContainer.classList.remove('active');
    });

    // Send message function
    function sendMessage() {
        const userMessage = userInput.value.trim();
        
        if (userMessage !== '') {
            // Add user message to chat
            addMessage(userMessage, 'user');
            
            // Clear input
            userInput.value = '';
            
            // Show typing indicator
            showTypingIndicator();
            
            // Simulate assistant response after a delay
            setTimeout(() => {
                // Remove typing indicator
                removeTypingIndicator();
                
                // Add assistant response
                processResponse(userMessage);
            }, 1500);
        }
    }

    // Process user message and generate response
    function processResponse(userMessage) {
        // Simple rule-based responses (would be replaced with actual backend API call)
        let botResponse = "I'm sorry, I don't have enough information to answer that. Could you provide more details?";
        
        userMessage = userMessage.toLowerCase();
        
        if (userMessage.includes('hello') || userMessage.includes('hi')) {
            botResponse = "Hello! How are you feeling today?";
        } else if (userMessage.includes('headache') || userMessage.includes('head pain')) {
            botResponse = "I'm sorry to hear you have a headache. Make sure you're hydrated, and consider taking a break from screens. If it persists, please consult your doctor.";
        } else if (userMessage.includes('cold') || userMessage.includes('flu') || userMessage.includes('fever')) {
            botResponse = "Rest is important when fighting a cold or flu. Stay hydrated, take over-the-counter medication as directed, and see a doctor if symptoms worsen or persist for more than a week.";
        } else if (userMessage.includes('diet') || userMessage.includes('nutrition')) {
            botResponse = "A balanced diet rich in fruits, vegetables, whole grains, lean proteins, and healthy fats is important for overall health. Would you like specific dietary recommendations?";
        } else if (userMessage.includes('exercise') || userMessage.includes('workout')) {
            botResponse = "Regular physical activity is crucial for health. Aim for at least 150 minutes of moderate aerobic activity or 75 minutes of vigorous activity each week, plus muscle-strengthening activities twice a week.";
        } else if (userMessage.includes('stress') || userMessage.includes('anxiety')) {
            botResponse = "Managing stress is important for both mental and physical health. Consider techniques like deep breathing, meditation, regular exercise, or speaking with a mental health professional.";
        }
        
        addMessage(botResponse, 'bot');
    }

    // Add message to chat
    function addMessage(text, sender) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', `${sender}-message`);
        messageElement.textContent = text;
        
        messageArea.appendChild(messageElement);
        
        // Scroll to bottom
        messageArea.scrollTop = messageArea.scrollHeight;
    }

    // Show typing indicator
    function showTypingIndicator() {
        const typingIndicator = document.createElement('div');
        typingIndicator.classList.add('message', 'bot-message', 'typing-indicator');
        typingIndicator.innerHTML = '<span></span><span></span><span></span>';
        typingIndicator.id = 'typing-indicator';
        
        messageArea.appendChild(typingIndicator);
        messageArea.scrollTop = messageArea.scrollHeight;
    }

    // Remove typing indicator
    function removeTypingIndicator() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }

    // Event listeners for sending messages
    sendBtn.addEventListener('click', sendMessage);
    
    userInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Initialize with greeting message
    initialMessages.forEach(msg => {
        addMessage(msg.text, msg.sender);
    });
});

// Global variables
let recognition;
let isRecording = false;
let synth = window.speechSynthesis;
let voices = [];

function createAssistantUI() {
    // Create floating button
    const floatingButton = document.createElement('div');
    floatingButton.id = 'health-assistant-btn';
    floatingButton.innerHTML = '<i class="fas fa-heartbeat"></i>';
    floatingButton.setAttribute('title', 'Health Assistant');
    document.body.appendChild(floatingButton);
    
    // Create chat container
    const chatContainer = document.createElement('div');
    chatContainer.id = 'health-assistant-container';
    chatContainer.classList.add('hidden');
    
    chatContainer.innerHTML = `
        <div class="chat-header">
            <div class="assistant-title">
                <i class="fas fa-heartbeat"></i>
                <span>Health Assistant</span>
            </div>
            <div class="header-controls">
                <button id="minimize-btn" title="Minimize"><i class="fas fa-minus"></i></button>
                <button id="close-btn" title="Close"><i class="fas fa-times"></i></button>
            </div>
        </div>
        <div class="chat-messages" id="chat-messages">
            <div class="message assistant">
                <div class="message-content">
                    Hello! I'm your Cardio Guide Health Assistant. I can help with heart health tips and answer your questions about cardiovascular wellness. How can I assist you today?
                </div>
            </div>
        </div>
        <div class="chat-input-area">
            <textarea id="user-input" placeholder="Type your health question here..."></textarea>
            <div class="input-controls">
                <button id="voice-btn" title="Voice Input">
                    <i class="fas fa-microphone"></i>
                </button>
                <button id="send-btn" title="Send">
                    <i class="fas fa-paper-plane"></i>
                </button>
            </div>
        </div>
    `;
    
    document.body.appendChild(chatContainer);
}

function initializeSpeech() {
    // Initialize speech recognition if supported
    if ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window) {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        recognition = new SpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'en-US';
        
        recognition.onresult = function(event) {
            const transcript = event.results[0][0].transcript;
            document.getElementById('user-input').value = transcript;
            isRecording = false;
            updateMicrophoneIcon();
        };
        
        recognition.onerror = function(event) {
            console.error('Speech recognition error:', event.error);
            isRecording = false;
            updateMicrophoneIcon();
        };
        
        recognition.onend = function() {
            isRecording = false;
            updateMicrophoneIcon();
        };
    }
    
    // Initialize speech synthesis
    if ('speechSynthesis' in window) {
        synth = window.speechSynthesis;
        // Load voices when available
        synth.onvoiceschanged = function() {
            voices = synth.getVoices();
        };
    }
}

function updateMicrophoneIcon() {
    const voiceBtn = document.getElementById('voice-btn');
    if (voiceBtn) {
        if (isRecording) {
            voiceBtn.innerHTML = '<i class="fas fa-stop"></i>';
            voiceBtn.classList.add('recording');
        } else {
            voiceBtn.innerHTML = '<i class="fas fa-microphone"></i>';
            voiceBtn.classList.remove('recording');
        }
    }
}

function toggleVoiceInput() {
    if (!recognition) {
        addMessage('Your browser does not support voice input.', 'assistant');
        return;
    }
    
    if (isRecording) {
        recognition.stop();
    } else {
        recognition.start();
        isRecording = true;
    }
    
    updateMicrophoneIcon();
}

function attachEventListeners() {
    // Toggle chat visibility when floating button is clicked
    document.getElementById('health-assistant-btn').addEventListener('click', function() {
        const container = document.getElementById('health-assistant-container');
        container.classList.toggle('hidden');
    });
    
    // Close chat when close button is clicked
    document.getElementById('close-btn').addEventListener('click', function() {
        document.getElementById('health-assistant-container').classList.add('hidden');
    });
    
    // Minimize chat when minimize button is clicked
    document.getElementById('minimize-btn').addEventListener('click', function() {
        document.getElementById('health-assistant-container').classList.add('hidden');
    });
    
    // Send message when send button is clicked
    document.getElementById('send-btn').addEventListener('click', sendMessage);
    
    // Send message when Enter key is pressed (without Shift)
    document.getElementById('user-input').addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
    
    // Toggle voice input when voice button is clicked
    document.getElementById('voice-btn').addEventListener('click', toggleVoiceInput);
}

function sendMessage() {
    const inputField = document.getElementById('user-input');
    const message = inputField.value.trim();
    
    if (message === '') return;
    
    // Add user message to the chat
    addUserMessage(message);
    
    // Clear input field
    inputField.value = '';
    
    // Show typing indicator
    showTypingIndicator();
    
    // Send the message to the server
    fetch('/api/health-assistant', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        // Hide typing indicator
        hideTypingIndicator();
        
        if (data.status === 'success') {
            // Add bot response to the chat
            addBotMessage(data.response);
        } else {
            // Handle error
            addBotMessage("I'm sorry, I'm having trouble processing your request right now. Please try again later.");
        }
    })
    .catch(error => {
        // Hide typing indicator
        hideTypingIndicator();
        
        // Add error message
        addBotMessage("I'm sorry, I'm having trouble connecting right now. Please check your connection and try again.");
        console.error('Error:', error);
    });
}

function addUserMessage(message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', 'user-message');
    messageElement.textContent = message;
    document.getElementById('health-assistant-messages').appendChild(messageElement);
    scrollToBottom();
}

function addBotMessage(message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', 'bot-message');
    messageElement.textContent = message;
    document.getElementById('health-assistant-messages').appendChild(messageElement);
    scrollToBottom();
}

function showTypingIndicator() {
    const typingIndicator = document.createElement('div');
    typingIndicator.id = 'typing-indicator';
    typingIndicator.classList.add('message', 'bot-message', 'typing-indicator');
    
    // Add the dots
    for (let i = 0; i < 3; i++) {
        const dot = document.createElement('span');
        dot.classList.add('dot');
        typingIndicator.appendChild(dot);
    }
    
    document.getElementById('health-assistant-messages').appendChild(typingIndicator);
    scrollToBottom();
}

function hideTypingIndicator() {
    const typingIndicator = document.getElementById('typing-indicator');
    if (typingIndicator) {
        typingIndicator.remove();
    }
}

function scrollToBottom() {
    const messagesContainer = document.getElementById('health-assistant-messages');
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
} 