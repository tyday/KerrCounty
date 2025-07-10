# Kerr County Minutes AI App Context

## Overview
- **Purpose**: Help users search, summarize, and analyze Kerr County meeting minutes with AI-powered insights
- **Users**: Researchers, journalists, citizens, AI systems (Claude via MCP)
- **Integration**: Expose functionality through MCP server for seamless AI assistant access

## Core Features
- **Multi-modal search**: Full-text, semantic (FAISS), and temporal filtering
- **Intelligent summarization**: Document summaries and cross-meeting trend analysis
- **AI Q&A**: Answer user questions based on document corpus
- **Topic extraction**: Identify recurring themes (emergency preparedness, budget, infrastructure)
- **Timeline analysis**: Track policy evolution and decision patterns over time
- **Cross-referencing**: Link related discussions across different meeting dates

## Data Architecture
- **Sources**: TXT and PDF files, organized by year in `minutes/` folder
- **Structured metadata**: Parse meeting structure (date, attendees, agenda items, votes, decisions)
- **Document chunking**: Intelligent segmentation for semantic search optimization
- **Indexing**: Pre-built indexes for emergency/flood-related terms and common government topics

## AI/ML Stack
- **Primary AI**: OpenAI API for summarization, Q&A, and topic extraction
- **Semantic search**: FAISS for vector similarity
- **Caching**: Redis for frequent queries and computed results
- **MCP Integration**: Custom MCP server exposing search and analysis functions

## MCP Server Functions
```typescript
// Core search and retrieval
search_minutes(query: string, date_range?: DateRange, topics?: string[])
get_meeting_by_date(date: string)
list_meetings(date_range?: DateRange)

// Analysis functions
analyze_topic_trends(topic: string, timeframe: string)
get_meeting_summary(date: string)
find_related_meetings(meeting_id: string)
extract_policy_timeline(topic: string)

// Specialized queries for current events
search_emergency_preparedness()
find_budget_allocations(category: string)
track_infrastructure_decisions()
```

## UI Components
- **Web app**: React-based interface with timeline visualization
- **Search interface**: Advanced filtering (date range, topics, participants)
- **Results display**: Hierarchical view with meeting context and related suggestions
- **Upload system**: New file ingestion with automatic processing
- **Export functionality**: Download summaries, search results, and analysis reports

## Deployment & Integration
- **Local server**: No authentication initially
- **MCP endpoint**: Separate port for AI system access
- **API documentation**: OpenAPI spec for MCP functions
- **Configuration**: Easy setup for Claude MCP client integration

## Enhanced Features for Flood Research
- **Emergency tracking**: Pre-configured searches for flood, emergency, disaster preparedness
- **Budget analysis**: Track funding decisions related to infrastructure and emergency services
- **Policy evolution**: Visualize how emergency preparedness policies changed over time
- **Cross-reference alerts**: Automatically suggest related meetings when viewing flood-related content

## Stretch Goals
- **User accounts**: Save searches and create custom alerts
- **Analytics dashboard**: Meeting participation, topic frequency, decision patterns
- **Real-time integration**: Auto-download new meeting minutes
- **Multi-county support**: Expand to other Texas counties
- **Advanced NLP**: Named entity recognition for people, places, and organizations

## Iterative Development Plan

### Phase 1: Bare Bones MCP Access (Week 1)
**Goal**: Get Claude connected and reading files
- **File system**: Basic file reader for TXT files in `minutes/` folder
- **MCP server**: Minimal server with 2 functions:
  - `list_files()` - Return available meeting files
  - `read_file(filename)` - Return raw file content
- **No AI processing** - Just file access
- **Test**: Verify Claude can list and read files through MCP

### Phase 2: Basic Search + Testing (Week 2)
**Goal**: Add simple search and validate Claude integration
- **Simple search**: Basic string matching across files
- **MCP functions**:
  - `search_text(query)` - Find files containing query string
  - `get_file_metadata(filename)` - Return file info (date, size)
- **Testing with Claude**: 
  - Search for "flood" or "emergency" terms
  - Test file retrieval and content analysis
  - Validate MCP connection stability

### Phase 3: Enhanced Search + Metadata (Week 3)
**Goal**: Add structured data and better search
- **Metadata parsing**: Extract meeting dates, attendees from file headers
- **Enhanced search**: 
  - Date range filtering
  - Multiple keyword support
- **MCP functions**:
  - `search_by_date_range(start_date, end_date)`
  - `search_with_filters(query, filters)`
- **Test**: Complex queries with Claude for flood research

### Phase 4: AI Integration + Analysis (Week 4)
**Goal**: Add OpenAI integration and topic analysis
- **OpenAI integration**: Summarization and Q&A
- **Topic extraction**: Basic keyword identification
- **MCP functions**:
  - `summarize_meeting(filename)`
  - `answer_question(query, context_files)`
- **Test**: Ask Claude to analyze patterns across meetings

### Phase 5: Advanced Features (Week 5+)
**Goal**: Add semantic search and cross-referencing
- **FAISS integration**: Vector similarity search
- **Cross-referencing**: Link related meetings
- **Timeline analysis**: Track topics over time
- **Full UI**: React web interface

## Development Testing Strategy
- **After each phase**: Test MCP connection with Claude
- **Document issues**: Keep log of Claude integration problems
- **Validate functions**: Ensure each MCP function works as expected
- **Performance check**: Monitor response times and reliability

This iterative approach ensures you have a working Claude integration from day one, then build complexity gradually while maintaining that connection.