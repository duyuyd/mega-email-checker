#!/usr/bin/env python3
"""
Service Testing Script - Debug each service individually
"""

import requests
import json
import time

def test_google(email):
    """Test Google service"""
    print(f"\n🔍 Testing Google for: {email}")
    
    # Check if Gmail
    if email.endswith('@gmail.com'):
        print("✅ Gmail domain - Google account always exists")
        return True
    
    try:
        username = email.split('@')[0]
        url = f'https://accounts.google.com/_/signup/webusernameavailability?username={username}'
        
        response = requests.get(url, timeout=10)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text[:200]}")
        
        if 'NAME_NOT_AVAILABLE' in response.text:
            print("✅ Google account EXISTS")
            return True
        else:
            print("❌ Google account NOT FOUND")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_twitter(email):
    """Test Twitter service"""
    print(f"\n🐦 Testing Twitter for: {email}")
    
    try:
        url = 'https://api.twitter.com/i/users/email_available.json'
        params = {'email': email}
        headers = {
            'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        }
        
        response = requests.get(url, params=params, headers=headers, timeout=10)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
            
            if data.get('valid') is False:
                print("✅ Twitter account EXISTS")
                return True
            else:
                print("❌ Twitter account NOT FOUND")
                return False
        else:
            print(f"❌ API Error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_netflix(email):
    """Test Netflix service"""
    print(f"\n🎬 Testing Netflix for: {email}")
    
    try:
        url = 'https://www.netflix.com/login'
        data = {'userLoginId': email}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.post(url, data=data, headers=headers, timeout=10)
        print(f"Status: {response.status_code}")
        
        # Check for various indicators
        text = response.text.lower()
        
        if 'password' in text:
            print("✅ Netflix account EXISTS (password field found)")
            return True
        elif 'incorrect password' in text:
            print("✅ Netflix account EXISTS (incorrect password)")
            return True
        elif 'sorry, we can\'t find' in text:
            print("❌ Netflix account NOT FOUND")
            return False
        else:
            print("⚠️  Could not determine")
            print(f"Response snippet: {response.text[:500]}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("🔧 SERVICE TESTING TOOL")
    print("=" * 50)
    
    email = input("Enter email to test: ").strip()
    
    if '@' not in email:
        print("❌ Invalid email!")
        return
    
    print(f"\nTesting email: {email}")
    print("=" * 30)
    
    # Test each service
    google_result = test_google(email)
    time.sleep(1)
    
    twitter_result = test_twitter(email)
    time.sleep(1)
    
    netflix_result = test_netflix(email)
    
    print(f"\n{'='*50}")
    print("📊 TEST SUMMARY:")
    print(f"Google: {'✅' if google_result else '❌'}")
    print(f"Twitter: {'✅' if twitter_result else '❌'}")
    print(f"Netflix: {'✅' if netflix_result else '❌'}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
