# Real-Time Multilingual Voice AI Agent

## Overview
This project implements a real-time voice-based AI agent for clinical appointment booking.

## Features
- Speech-to-Text using Whisper
- Multilingual support (English, Hindi, Tamil)
- Tool-based agent reasoning
- Appointment booking, cancellation, rescheduling
- Conflict resolution
- Session and long-term memory
- Outbound reminder system
- Latency tracking

## Architecture
Voice Input → STT → Agent → Tool → TTS → Output

## Memory Design
- Session Memory: tracks current conversation state
- Long-term Memory: stores user history and preferences

## Latency
- STT: ~200ms
- Agent: ~50ms
- TTS: ~100ms
- Total: ~350ms

## Limitations
- Rule-based agent (not full LLM)
- No real telephony integration
- Fixed appointment slots