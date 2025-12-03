#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MEGA EMAIL CHECKER PRO - FAST & ACCURATE
# DEVELOPED BY MR DUYKA

import requests
import time
import json
import random
import sys
import os
import re
import threading
import queue
from datetime import datetime
from colorama import init, Fore, Style
from concurrent.futures import ThreadPoolExecutor, as_completed

init(autoreset=True)

class MegaEmailChecker:
    def __init__(self):
        self.version = "8.0 FAST & SMART"
        self.developer = "MR DUYKA"
        self.results_file = "checked_emails.txt"
        self.cache_file = "email_cache.json"
        self.cache = self.load_cache()
        
        # SMART SERVICES với timeout ngắn hơn
        self.services = {
            "Facebook": {"emoji": "👤", "color": Fore.BLUE, "timeout": 8, "smart_check": True},
            "Google": {"emoji": "📧", "color": Fore.RED, "timeout": 3, "smart_check": True},
            "Instagram": {"emoji": "📷", "color": Fore.MAGENTA, "timeout": 6, "smart_check": True},
            "Twitter": {"emoji": "🐦", "color": Fore.CYAN, "timeout": 5, "smart_check": True},
            "TikTok": {"emoji": "📱", "color": Fore.BLACK, "timeout": 6, "smart_check": True},
            "Netflix": {"emoji": "🎬", "color": Fore.RED, "timeout": 5, "smart_check": True},
            "PayPal": {"emoji": "💰", "color": Fore.BLUE, "timeout": 5, "smart_check": True},
            "Discord": {"emoji": "🎮", "color": Fore.CYAN, "timeout": 5, "smart_check": True},
            "Microsoft": {"emoji": "🪟", "color": Fore.BLUE, "timeout": 5, "smart_check": True},
            "Amazon": {"emoji": "📦", "color": Fore.YELLOW, "timeout": 5, "smart_check": True},
            "LinkedIn": {"emoji": "💼", "color": Fore.BLUE, "timeout": 5, "smart_check": True},
            "GitHub": {"emoji": "💻", "color": Fore.WHITE, "timeout": 5, "smart_check": True},
            "Spotify": {"emoji": "🎵", "color": Fore.GREEN, "timeout": 5, "smart_check": True},
            "Snapchat": {"emoji": "👻", "color": Fore.YELLOW, "timeout": 5, "smart_check": False},
            "Pinterest": {"emoji": "📌", "color": Fore.RED, "timeout": 5, "smart_check": False},
            "Reddit": {"emoji": "👽", "color": Fore.RED, "timeout": 5, "smart_check": False},
        }
        
        # User-Agents thông minh
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15',
        ]
        
        self.checked_count = 0
        self.session_pool = {}
        self.request_timeout = 10
        self.max_workers = 5  # Số thread tối đa

    def load_cache(self):
        """Load cache từ file"""
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def save_cache(self):
        """Lưu cache vào file"""
        try:
            with open(self.cache_file, 'w') as f:
                json.dump(self.cache, f)
        except:
            pass

    def get_session(self):
        """Get hoặc tạo session mới"""
        thread_id = threading.get_ident()
        if thread_id not in self.session_pool:
            session = requests.Session()
            session.headers.update({
                'User-Agent': random.choice(self.user_agents),
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
            })
            self.session_pool[thread_id] = session
        return self.session_pool[thread_id]

    # ========== SMART CHECK METHODS ==========
    
    def smart_check_google(self, email):
        """Google check cực nhanh"""
        if email.lower().endswith('@gmail.com'):
            return True  # Gmail luôn có account
        
        try:
            # Check nhanh qua Google API
            session = self.get_session()
            response = session.head(
                f'https://mail.google.com/mail/gxlu?email={email}',
                timeout=3,
                allow_redirects=True
            )
            # Nếu có cookie Set-Cookie với GMAIL, account exists
            if 'Set-Cookie' in response.headers and 'GMAIL' in response.headers['Set-Cookie'].upper():
                return True
        except:
            pass
        
        # Fallback: Check qua signup
        try:
            username = email.split('@')[0]
            session = self.get_session()
            response = session.get(
                f'https://accounts.google.com/InputValidator?Email={username}',
                timeout=3
            )
            return 'Taken' in response.text
        except:
            return False

    def smart_check_facebook(self, email):
        """Facebook check thông minh"""
        # Kiểm tra cache trước
        cache_key = f"fb_{email}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            # Method 1: Head request nhanh
            session = self.get_session()
            response = session.head(
                f'https://www.facebook.com/{email}',
                timeout=5,
                allow_redirects=True
            )
            
            # Nếu không redirect đến trang lỗi, có thể account exists
            if response.status_code == 200 and 'facebook' in response.url:
                self.cache[cache_key] = True
                return True
            
            # Method 2: Check qua mobile
            response = session.get(
                f'https://m.facebook.com/{email}',
                timeout=5,
                allow_redirects=False
            )
            
            # Facebook thường redirect nếu account không tồn tại
            if response.status_code == 200 and 'content="m.facebook.com"' in response.text:
                self.cache[cache_key] = True
                return True
                
        except:
            pass
        
        # Default: return False và cache kết quả
        self.cache[cache_key] = False
        return False

    def smart_check_twitter(self, email):
        """Twitter check nhanh"""
        try:
            session = self.get_session()
            # Twitter có API public để check email
            response = session.get(
                'https://api.twitter.com/i/users/email_available.json',
                params={'email': email},
                timeout=4
            )
            
            if response.status_code == 200:
                data = response.json()
                # Nếu valid = false, email đã được sử dụng
                return not data.get('valid', True)
        except:
            pass
        return False

    def smart_check_tiktok(self, email):
        """TikTok check thông minh"""
        try:
            session = self.get_session()
            # TikTok check qua signup API
            response = session.post(
                'https://www.tiktok.com/api/user/check_email/',
                json={'email': email},
                timeout=5
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get('data', {}).get('exist', False)
        except:
            pass
        return False

    def smart_check_instagram(self, email):
        """Instagram check nhanh"""
        try:
            session = self.get_session()
            # Instagram check qua password reset
            response = session.post(
                'https://www.instagram.com/accounts/account_recovery_send_ajax/',
                data={'email_or_username': email},
                timeout=5
            )
            
            if response.status_code == 200:
                return 'user' in response.text.lower()
        except:
            pass
        return False

    def smart_check_netflix(self, email):
        """Netflix check nhanh"""
        try:
            session = self.get_session()
            response = session.post(
                'https://www.netflix.com/login',
                data={'userLoginId': email},
                timeout=5
            )
            return 'password' in response.text.lower()
        except:
            return False

    def smart_check_paypal(self, email):
        """PayPal check nhanh"""
        try:
            session = self.get_session()
            response = session.post(
                'https://www.paypal.com/authflow/password-recovery/',
                data={'email': email},
                timeout=5
            )
            return 'recovery' in response.text.lower()
        except:
            return False

    def smart_check_discord(self, email):
        """Discord check nhanh"""
        try:
            session = self.get_session()
            response = session.post(
                'https://discord.com/api/v9/auth/register',
                json={'email': email, 'username': 'test123'},
                timeout=5
            )
            return response.status_code == 400 and 'EMAIL' in response.text
        except:
            return False

    def smart_check_microsoft(self, email):
        """Microsoft check nhanh"""
        try:
            session = self.get_session()
            response = session.post(
                'https://login.live.com/GetCredentialType.srf',
                json={'Username': email},
                timeout=5
            )
            if response.status_code == 200:
                data = response.json()
                return data.get('IfExistsResult') == 0
        except:
            return False

    def smart_check_amazon(self, email):
        """Amazon check nhanh"""
        try:
            session = self.get_session()
            response = session.post(
                'https://www.amazon.com/ap/signin',
                data={'email': email},
                timeout=5
            )
            return 'password' in response.text.lower()
        except:
            return False

    def smart_check_linkedin(self, email):
        """LinkedIn check nhanh"""
        try:
            session = self.get_session()
            response = session.post(
                'https://www.linkedin.com/uas/request-password-reset',
                data={'userName': email},
                timeout=5
            )
            return 'reset' in response.text.lower()
        except:
            return False

    def smart_check_github(self, email):
        """GitHub check nhanh"""
        try:
            session = self.get_session()
            response = session.post(
                'https://github.com/password_reset',
                data={'email': email},
                timeout=5
            )
            return 'check your email' in response.text.lower()
        except:
            return False

    def smart_check_spotify(self, email):
        """Spotify check nhanh"""
        try:
            session = self.get_session()
            response = session.post(
                'https://www.spotify.com/api/signup/validate',
                json={'email': email},
                timeout=5
            )
            if response.status_code == 200:
                data = response.json()
                return data.get('status') == 20
        except:
            return False

    # ========== CORE CHECK FUNCTION ==========
    
    def check_service(self, service_name, email):
        """Check service với timeout và caching"""
        service_info = self.services.get(service_name)
        if not service_info:
            return False
        
        # Check cache trước
        cache_key = f"{service_name}_{email}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        result = False
        method_name = f"smart_check_{service_name.lower().replace('/', '_').replace('-', '_')}"
        
        try:
            method = getattr(self, method_name, None)
            if method:
                result = method(email)
            else:
                result = False
        except:
            result = False
        
        # Lưu vào cache
        self.cache[cache_key] = result
        return result

    def check_single_email_fast(self, email):
        """Check email nhanh với multi-threading"""
        print(f"\n{Fore.CYAN}{'═'*60}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}⚡ FAST CHECKING: {email}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'═'*60}{Style.RESET_ALL}")
        
        start_time = time.time()
        results = {}
        
        # Tạo task queue
        tasks = []
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit tất cả tasks
            future_to_service = {}
            for service_name in self.services.keys():
                future = executor.submit(self.check_service, service_name, email)
                future_to_service[future] = service_name
                time.sleep(0.1)  # Small delay để tránh rate limit
            
            # Process results khi hoàn thành
            completed = 0
            total = len(self.services)
            
            for future in as_completed(future_to_service):
                service_name = future_to_service[future]
                service_info = self.services[service_name]
                emoji = service_info['emoji']
                color = service_info['color']
                
                completed += 1
                try:
                    result = future.result(timeout=10)
                except:
                    result = False
                
                results[service_name] = result
                
                # Hiển thị progress
                service_display = f"{service_name:12}"
                status = f"{Fore.GREEN}✅ FOUND" if result else f"{Fore.RED}❌ NOT FOUND"
                print(f"[{completed:2d}/{total}] {emoji} {color}{service_display}{Style.RESET_ALL} {status}")
        
        elapsed_time = time.time() - start_time
        self.checked_count += 1
        self.save_cache()  # Lưu cache
        
        return results, elapsed_time

    def check_single_email_smart(self, email):
        """Check email với smart logic (chỉ check services quan trọng)"""
        print(f"\n{Fore.CYAN}{'═'*60}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🤖 SMART CHECKING: {email}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'═'*60}{Style.RESET_ALL}")
        
        start_time = time.time()
        results = {}
        
        # Chỉ check các services smart_check = True trước
        smart_services = {k: v for k, v in self.services.items() if v.get('smart_check', False)}
        
        print(f"{Fore.YELLOW}[*] Checking {len(smart_services)} smart services first...{Style.RESET_ALL}\n")
        
        for idx, (service_name, service_info) in enumerate(smart_services.items(), 1):
            emoji = service_info['emoji']
            color = service_info['color']
            
            service_display = f"{service_name:12}"
            print(f"[{idx:2d}/{len(smart_services)}] {emoji} {color}{service_display}{Style.RESET_ALL} Checking...", end=' ')
            
            result = self.check_service(service_name, email)
            results[service_name] = result
            
            if result:
                print(f"{Fore.GREEN}✅ FOUND{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}❌ NOT FOUND{Style.RESET_ALL}")
            
            # Delay ngắn
            time.sleep(0.3)
        
        # Hỏi user có muốn check thêm services không
        remaining_services = set(self.services.keys()) - set(smart_services.keys())
        if remaining_services:
            print(f"\n{Fore.YELLOW}[?] Check remaining {len(remaining_services)} services? (y/n): {Style.RESET_ALL}", end=' ')
            choice = input().strip().lower()
            
            if choice == 'y':
                for service_name in remaining_services:
                    service_info = self.services[service_name]
                    emoji = service_info['emoji']
                    color = service_info['color']
                    
                    service_display = f"{service_name:12}"
                    print(f"[+] {emoji} {color}{service_display}{Style.RESET_ALL} Checking...", end=' ')
                    
                    result = self.check_service(service_name, email)
                    results[service_name] = result
                    
                    if result:
                        print(f"{Fore.GREEN}✅ FOUND{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.RED}❌ NOT FOUND{Style.RESET_ALL}")
                    
                    time.sleep(0.2)
        
        elapsed_time = time.time() - start_time
        self.checked_count += 1
        self.save_cache()
        
        return results, elapsed_time

    def show_results(self, email, results, elapsed_time, mode="FAST"):
        """Hiển thị kết quả"""
        print(f"\n{Fore.CYAN}{'═'*60}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}          CHECK RESULTS - {mode} MODE{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'═'*60}{Style.RESET_ALL}")
        
        print(f"{Fore.WHITE}📧 Email: {Fore.CYAN}{email}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}⏱️  Time: {Fore.YELLOW}{elapsed_time:.1f} seconds{Style.RESET_ALL}")
        print(f"{Fore.WHITE}🚀 Mode: {Fore.GREEN}{mode}{Style.RESET_ALL}")
        
        # Gmail special note
        if email.lower().endswith('@gmail.com'):
            print(f"{Fore.GREEN}📝 Note: Gmail address - Google account exists{Style.RESET_ALL}")
        
        found_services = [s for s, found in results.items() if found]
        
        if found_services:
            print(f"\n{Fore.GREEN}✅ ACCOUNTS FOUND ({len(found_services)}):{Style.RESET_ALL}")
            # Nhóm theo category
            primary = []
            secondary = []
            
            for service in found_services:
                if service in ["Facebook", "Google", "Instagram", "Twitter", "TikTok"]:
                    primary.append(service)
                else:
                    secondary.append(service)
            
            if primary:
                print(f"{Fore.CYAN}   Primary:{Style.RESET_ALL}")
                for service in primary:
                    emoji = self.services[service]['emoji']
                    color = self.services[service]['color']
                    print(f"     {emoji} {color}{service}{Style.RESET_ALL}")
            
            if secondary:
                print(f"{Fore.CYAN}   Secondary:{Style.RESET_ALL}")
                for service in secondary:
                    emoji = self.services[service]['emoji']
                    color = self.services[service]['color']
                    print(f"     {emoji} {color}{service}{Style.RESET_ALL}")
            
            # Statistics
            total_checked = len(results)
            success_rate = (len(found_services) / total_checked * 100) if total_checked > 0 else 0
            
            print(f"\n{Fore.YELLOW}📊 Statistics:{Style.RESET_ALL}")
            print(f"   • Found: {len(found_services)}/{total_checked}")
            print(f"   • Success rate: {success_rate:.1f}%")
            print(f"   • Primary services: {len(primary)}")
            print(f"   • Cache hits: {self.get_cache_stats(email)}")
            
        else:
            print(f"\n{Fore.RED}❌ NO ACCOUNTS FOUND{Style.RESET_ALL}")
            print(f"   {Fore.YELLOW}Email not registered on checked platforms{Style.RESET_ALL}")
        
        print(f"\n{Fore.CYAN}⚡ Performance:{Style.RESET_ALL}")
        print(f"   • Time per service: {(elapsed_time/len(results)):.1f}s")
        print(f"   • Mode: {mode}")
        print(f"   • Using cache: {len(self.cache)} entries")
        print(f"   • Results saved to: {self.results_file}")

    def get_cache_stats(self, email):
        """Get cache statistics"""
        hits = 0
        total = len(self.services)
        for service in self.services:
            cache_key = f"{service}_{email}"
            if cache_key in self.cache:
                hits += 1
        return f"{hits}/{total}"

    def save_results(self, email, results):
        """Lưu kết quả"""
        try:
            with open(self.results_file, 'a', encoding='utf-8') as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                found_services = [s for s, found in results.items() if found]
                
                f.write(f"\n{'═'*60}\n")
                f.write(f"📧 Email: {email}\n")
                f.write(f"⏰ Time: {timestamp}\n")
                f.write(f"📊 Found: {len(found_services)}/{len(results)}\n")
                
                if found_services:
                    f.write("✅ Accounts:\n")
                    for service in found_services:
                        emoji = self.services[service]['emoji']
                        f.write(f"   {emoji} {service}\n")
                f.write(f"{'═'*60}\n")
        except Exception as e:
            print(f"{Fore.RED}[!] Error saving: {e}{Style.RESET_ALL}")

    def clear_cache(self):
        """Xóa cache"""
        self.cache = {}
        self.save_cache()
        print(f"{Fore.GREEN}[✓] Cache cleared!{Style.RESET_ALL}")

    def show_banner(self):
        banner = f"""
{Fore.CYAN}
╔╦╗┬┌─┐┌─┐┌─┐  ╔╦╗┌─┐┌┐┌┌─┐┬┌─┐┬┌─┐  ╔═╗┌─┐┬─┐┌─┐┌─┐
 ║ ├┴┐├┤ ├─┤   ║║║├─┤│││├┤ ││ ┬│└─┐  ╠═╝├┤ ├┬┘└─┐├┤ 
 ╩ ┴ ┴└─┘┴ ┴  ═╩╝┴┴ ┴┘└┘└─┘┴└─┘┴└─┘  ╩  └─┘┴└─└─┘└─┘
{Style.RESET_ALL}
{Fore.YELLOW}╔══════════════════════════════════════════════════╗{Style.RESET_ALL}
{Fore.YELLOW}║   MEGA EMAIL CHECKER v{self.version}              ║{Style.RESET_ALL}
{Fore.YELLOW}║        DEVELOPED BY {self.developer}                 ║{Style.RESET_ALL}
{Fore.YELLOW}╚══════════════════════════════════════════════════╝{Style.RESET_ALL}
{Fore.CYAN}[*] SERVICES     : {len(self.services)} PLATFORMS{Style.RESET_ALL}
{Fore.CYAN}[*] SPEED        : MULTI-THREADED + CACHING{Style.RESET_ALL}
{Fore.GREEN}[*] SMART MODE   : PRIORITIZED CHECKING{Style.RESET_ALL}
{Fore.YELLOW}[*] CACHE       : {len(self.cache)} ENTRIES{Style.RESET_ALL}
{Fore.RED}[*] WARNING     : USE RESPONSIBLY{Style.RESET_ALL}
"""
        print(banner)
    
    def show_menu(self):
        print(f"\n{Fore.CYAN}{'═'*60}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}          MEGA EMAIL CHECKER{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'═'*60}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}[1] {Fore.GREEN}⚡ Fast Check (Multi-threaded){Style.RESET_ALL}")
        print(f"{Fore.WHITE}[2] {Fore.BLUE}🤖 Smart Check (Priority-based){Style.RESET_ALL}")
        print(f"{Fore.WHITE}[3] {Fore.YELLOW}🎯 Check Specific Service{Style.RESET_ALL}")
        print(f"{Fore.WHITE}[4] {Fore.MAGENTA}📊 View Results / Cache{Style.RESET_ALL}")
        print(f"{Fore.WHITE}[5] {Fore.RED}🗑️  Clear Cache{Style.RESET_ALL}")
        print(f"{Fore.WHITE}[6] {Fore.CYAN}❓ About / Help{Style.RESET_ALL}")
        print(f"{Fore.WHITE}[7] {Fore.RED}🚪 Exit{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'═'*60}{Style.RESET_ALL}")

    def run_fast_check(self):
        """Option 1: Fast check với multi-threading"""
        print(f"\n{Fore.CYAN}[*] ⚡ FAST CHECK MODE{Style.RESET_ALL}")
        email = input(f"{Fore.WHITE}Enter email to check: {Style.RESET_ALL}").strip()
        
        if not email or '@' not in email:
            print(f"{Fore.RED}[!] Invalid email!{Style.RESET_ALL}")
            return
        
        print(f"\n{Fore.YELLOW}[*] Starting fast check with {self.max_workers} threads...{Style.RESET_ALL}")
        
        results, elapsed_time = self.check_single_email_fast(email)
        self.show_results(email, results, elapsed_time, "FAST")
        self.save_results(email, results)
        
        input(f"\n{Fore.YELLOW}[*] Press Enter to continue...{Style.RESET_ALL}")

    def run_smart_check(self):
        """Option 2: Smart check"""
        print(f"\n{Fore.CYAN}[*] 🤖 SMART CHECK MODE{Style.RESET_ALL}")
        email = input(f"{Fore.WHITE}Enter email to check: {Style.RESET_ALL}").strip()
        
        if not email or '@' not in email:
            print(f"{Fore.RED}[!] Invalid email!{Style.RESET_ALL}")
            return
        
        results, elapsed_time = self.check_single_email_smart(email)
        self.show_results(email, results, elapsed_time, "SMART")
        self.save_results(email, results)
        
        input(f"\n{Fore.YELLOW}[*] Press Enter to continue...{Style.RESET_ALL}")

    def run_specific_check(self):
        """Option 3: Check specific service"""
        print(f"\n{Fore.CYAN}[*] 🎯 SPECIFIC SERVICE CHECK{Style.RESET_ALL}")
        
        print(f"{Fore.WHITE}Available services:{Style.RESET_ALL}")
        services = list(self.services.keys())
        for i, service in enumerate(services, 1):
            info = self.services[service]
            print(f"  {i:2d}. {info['emoji']} {info['color']}{service}{Style.RESET_ALL}")
        
        try:
            choice = int(input(f"\n{Fore.WHITE}Select service (1-{len(services)}): {Style.RESET_ALL}").strip())
            if 1 <= choice <= len(services):
                service_name = services[choice-1]
                email = input(f"{Fore.WHITE}Enter email: {Style.RESET_ALL}").strip()
                
                if email and '@' in email:
                    print(f"\n{Fore.YELLOW}[*] Checking {service_name} for {email}...{Style.RESET_ALL}")
                    
                    start = time.time()
                    result = self.check_service(service_name, email)
                    elapsed = time.time() - start
                    
                    info = self.services[service_name]
                    
                    print(f"\n{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
                    print(f"{info['emoji']} {info['color']}{service_name} RESULT{Style.RESET_ALL}")
                    print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
                    print(f"Email: {email}")
                    print(f"Time: {elapsed:.1f}s")
                    print(f"Result: {Fore.GREEN if result else Fore.RED}{'FOUND' if result else 'NOT FOUND'}{Style.RESET_ALL}")
                    print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}[!] Invalid email!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[!] Invalid choice!{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}[!] Please enter a number!{Style.RESET_ALL}")
        
        input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")

    def view_results_cache(self):
        """Option 4: View results and cache"""
        print(f"\n{Fore.CYAN}{'═'*60}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}          RESULTS & CACHE{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'═'*60}{Style.RESET_ALL}")
        
        # Hiển thị cache stats
        print(f"{Fore.WHITE}📊 Cache Statistics:{Style.RESET_ALL}")
        print(f"   • Total entries: {len(self.cache)}")
        
        # Hiển thị recent checks từ file
        if os.path.exists(self.results_file):
            try:
                with open(self.results_file, 'r') as f:
                    lines = f.readlines()[-50:]  # Last 50 lines
                    if lines:
                        print(f"\n{Fore.WHITE}📝 Recent Checks:{Style.RESET_ALL}")
                        print(''.join(lines[-10:]))  # Last 10 lines
                    else:
                        print(f"{Fore.YELLOW}[!] No results yet{Style.RESET_ALL}")
            except:
                print(f"{Fore.RED}[!] Error reading results{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}[!] No results file found{Style.RESET_ALL}")
        
        input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")

    def show_about(self):
        """Option 6: About"""
        print(f"\n{Fore.CYAN}{'═'*60}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}          ABOUT MEGA EMAIL CHECKER{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'═'*60}{Style.RESET_ALL}")
        
        print(f"{Fore.WHITE}🚀 Features:{Style.RESET_ALL}")
        print(f"   • {Fore.GREEN}Multi-threaded checking{Style.RESET_ALL}")
        print(f"   • {Fore.GREEN}Smart caching system{Style.RESET_ALL}")
        print(f"   • {Fore.GREEN}Priority-based checking{Style.RESET_ALL}")
        print(f"   • {Fore.GREEN}Fast timeout handling{Style.RESET_ALL}")
        
        print(f"\n{Fore.WHITE}⚡ Performance:{Style.RESET_ALL}")
        print(f"   • {Fore.CYAN}Check time: 15-30 seconds{Style.RESET_ALL}")
        print(f"   • {Fore.CYAN}Cache hits: Faster repeated checks{Style.RESET_ALL}")
        print(f"   • {Fore.CYAN}Smart logic: Check important services first{Style.RESET_ALL}")
        
        print(f"\n{Fore.WHITE}🔧 Technical:{Style.RESET_ALL}")
        print(f"   • {Fore.YELLOW}Version: {self.version}{Style.RESET_ALL}")
        print(f"   • {Fore.YELLOW}Services: {len(self.services)}{Style.RESET_ALL}")
        print(f"   • {Fore.YELLOW}Threads: {self.max_workers}{Style.RESET_ALL}")
        
        print(f"\n{Fore.RED}⚠️  Disclaimer:{Style.RESET_ALL}")
        print(f"   • For educational purposes only")
        print(f"   • Use responsibly")
        print(f"   • Respect privacy policies")
        
        input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")

    def run(self):
        """Main program"""
        self.show_banner()
        
        while True:
            try:
                self.show_menu()
                choice = input(f"\n{Fore.WHITE}Select option (1-7): {Style.RESET_ALL}").strip()
                
                if choice == '1':
                    self.run_fast_check()
                elif choice == '2':
                    self.run_smart_check()
                elif choice == '3':
                    self.run_specific_check()
                elif choice == '4':
                    self.view_results_cache()
                elif choice == '5':
                    self.clear_cache()
                elif choice == '6':
                    self.show_about()
                elif choice == '7':
                    print(f"\n{Fore.GREEN}[*] Thank you for using Mega Email Checker!{Style.RESET_ALL}")
                    print(f"{Fore.YELLOW}[*] Total checks: {self.checked_count}{Style.RESET_ALL}")
                    print(f"{Fore.CYAN}[*] Cache saved with {len(self.cache)} entries{Style.RESET_ALL}")
                    self.save_cache()
                    time.sleep(2)
                    break
                else:
                    print(f"{Fore.RED}[!] Invalid choice!{Style.RESET_ALL}")
            
            except KeyboardInterrupt:
                print(f"\n\n{Fore.YELLOW}[*] Exiting...{Style.RESET_ALL}")
                self.save_cache()
                break
            except Exception as e:
                print(f"\n{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")

def main():
    print(f"{Fore.YELLOW}[*] Starting Mega Email Checker v8.0...{Style.RESET_ALL}")
    time.sleep(1)
    
    checker = MegaEmailChecker()
    checker.run()

if __name__ == "__main__":
    main()
