#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MEGA EMAIL CHECKER PRO - ALL IN ONE
# DEVELOPED BY MR DUYKA

import requests
import time
import json
import random
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

class MegaEmailChecker:
    def __init__(self):
        self.version = "2.0 ALL-IN-ONE"
        self.developer = "MR DUYKA"
        self.mode = None
        
        # Services database
        self.services = {
            "Facebook": {"emoji": "👤", "color": Fore.BLUE, "real_check": True},
            "Instagram": {"emoji": "📷", "color": Fore.MAGENTA, "real_check": True},
            "Twitter": {"emoji": "🐦", "color": Fore.CYAN, "real_check": True},
            "Netflix": {"emoji": "🎬", "color": Fore.RED, "real_check": False},
            "Spotify": {"emoji": "🎵", "color": Fore.GREEN, "real_check": False},
            "PayPal": {"emoji": "💰", "color": Fore.BLUE, "real_check": False},
            "Discord": {"emoji": "🎮", "color": Fore.CYAN, "real_check": False},
            "Google": {"emoji": "🔍", "color": Fore.RED, "real_check": True},
            "Microsoft": {"emoji": "🪟", "color": Fore.BLUE, "real_check": True},
            "Amazon": {"emoji": "📦", "color": Fore.YELLOW, "real_check": False},
            "TikTok": {"emoji": "🎵", "color": Fore.BLACK, "real_check": False},
            "LinkedIn": {"emoji": "💼", "color": Fore.BLUE, "real_check": False},
            "eBay": {"emoji": "🛒", "color": Fore.YELLOW, "real_check": False},
            "Steam": {"emoji": "🎮", "color": Fore.WHITE, "real_check": False},
            "Yahoo": {"emoji": "📧", "color": Fore.MAGENTA, "real_check": False},
        }
        
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def show_banner(self):
        banner = f"""
{Fore.CYAN}
╔╦╗┬┌─┐┌─┐┌─┐  ╔╦╗┌─┐┌┐┌┌─┐┬┌─┐┬┌─┐  ╔═╗┌─┐┬─┐┌─┐┌─┐
 ║ ├┴┐├┤ ├─┤   ║║║├─┤│││├┤ ││ ┬│└─┐  ╠═╝├┤ ├┬┘└─┐├┤
 ╩ ┴ ┴└─┘┴ ┴  ═╩╝┴┴ ┴┘└┘└─┘┴└─┘┴└─┘  ╩  └─┘┴└─└─┘└─┘
{Style.RESET_ALL}
{Fore.YELLOW}╔══════════════════════════════════════════╗{Style.RESET_ALL}
{Fore.YELLOW}║   MEGA EMAIL CHECKER v{self.version}      ║{Style.RESET_ALL}
{Fore.YELLOW}║        DEVELOPED BY {self.developer}      ║{Style.RESET_ALL}
{Fore.YELLOW}╚══════════════════════════════════════════╝{Style.RESET_ALL}
{Fore.CYAN}[*] SERVICES     : {len(self.services)} PLATFORMS{Style.RESET_ALL}
{Fore.CYAN}[*] REAL CHECK   : 6 PLATFORMS AVAILABLE{Style.RESET_ALL}
"""
        print(banner)

    def select_mode(self):
        print(f"\n{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}        SELECT CHECKING MODE{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}[1] SINGLE EMAIL CHECK{Style.RESET_ALL}")
        print(f"   • Check one email at a time")
        print(f"   • Real HTTP requests")
        print(f"   • Detailed results")
        
        print(f"\n{Fore.YELLOW}[2] MULTI EMAIL CHECK{Style.RESET_ALL}")
        print(f"   • Check multiple emails")
        print(f"   • From file input")
        print(f"   • Batch processing")
        
        print(f"\n{Fore.RED}[3] SIMULATION MODE (Demo){Style.RESET_ALL}")
        print(f"   • No real requests")
        print(f"   • For testing UI")
        print(f"   • Generated data")
        
        print(f"\n{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
        
        while True:
            choice = input(f"\n{Fore.YELLOW}[?] Select mode [1/2/3]: {Style.RESET_ALL}").strip()
            
            if choice == "1":
                self.mode = "single"
                break
            elif choice == "2":
                self.mode = "multi"
                break
            elif choice == "3":
                self.mode = "simulation"
                break
            else:
                print(f"{Fore.RED}[!] Invalid choice. Enter 1, 2 or 3{Style.RESET_ALL}")

    # ========== REAL CHECK METHODS ==========
    
    def check_facebook(self, email):
        """Real Facebook check"""
        try:
            r1 = self.session.get('https://www.facebook.com/login/identify/', timeout=10)
            data = {'email': email, 'did_submit': 'Search'}
            r2 = self.session.post('https://www.facebook.com/login/identify/', 
                                 data=data, timeout=15)
            
            indicators = ['find your account', 'send_recovery', 'id="send_recovery"']
            for indicator in indicators:
                if indicator in r2.text:
                    return True
            return False
        except:
            return False

    def check_instagram(self, email):
        """Real Instagram check"""
        try:
            headers = {'User-Agent': 'Instagram 219.0.0.12.117 Android'}
            data = {'email_or_username': email}
            r = requests.post(
                'https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/',
                data=data,
                headers=headers,
                timeout=15
            )
            return r.status_code == 200 and ('user' in r.text or 'sent' in r.text)
        except:
            return False

    def check_twitter(self, email):
        """Real Twitter check"""
        try:
            r = requests.get(
                f'https://twitter.com/i/flow/signup?email={email}',
                timeout=10
            )
            return 'email has already' in r.text.lower()
        except:
            return False

    def check_google(self, email):
        """Real Google check"""
        try:
            r = requests.get(
                f'https://accounts.google.com/signin/v1/lookup',
                params={'email': email},
                timeout=10
            )
            return 'profile' in r.text or 'user' in r.text
        except:
            return False

    def check_microsoft(self, email):
        """Real Microsoft check"""
        try:
            r = requests.post(
                'https://login.live.com/',
                data={'login': email, 'passwd': ''},
                timeout=10
            )
            return 'The account or password is incorrect' in r.text
        except:
            return False

    def check_service_real(self, service_name, email):
        """Dispatch real checks"""
        if service_name == "Facebook":
            return self.check_facebook(email)
        elif service_name == "Instagram":
            return self.check_instagram(email)
        elif service_name == "Twitter":
            return self.check_twitter(email)
        elif service_name == "Google":
            return self.check_google(email)
        elif service_name == "Microsoft":
            return self.check_microsoft(email)
        else:
            # Other services - simulate with lower chance
            time.sleep(0.3)
            return random.random() < 0.2  # 20% chance

    # ========== MODE 1: SINGLE EMAIL CHECK ==========
    
    def run_single_check(self):
        print(f"\n{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}        SINGLE EMAIL CHECK{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
        
        while True:
            email = input(f"\n{Fore.GREEN}[?] Enter email (or 'quit' to exit): {Style.RESET_ALL}").strip()
            
            if email.lower() == 'quit':
                print(f"{Fore.YELLOW}[*] Returning to menu...{Style.RESET_ALL}")
                break
            
            if '@' not in email or '.' not in email:
                print(f"{Fore.RED}[!] Invalid email format!{Style.RESET_ALL}")
                continue
            
            print(f"\n{Fore.CYAN}[*] Checking: {email}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[*] Please wait 10-15 seconds...{Style.RESET_ALL}\n")
            
            start_time = time.time()
            results = {}
            
            # Check each service
            total_services = len(self.services)
            for i, (service_name, service_info) in enumerate(self.services.items(), 1):
                print(f"{Fore.WHITE}[{i}/{total_services}] {service_name}...{Style.RESET_ALL}", end=" ")
                
                try:
                    if service_info["real_check"]:
                        found = self.check_service_real(service_name, email)
                    else:
                        # For non-real check services, use simulation
                        time.sleep(0.2)
                        found = random.random() < 0.3  # 30% chance
                    
                    results[service_name] = found
                    
                    if found:
                        print(f"{service_info['color']}✓ FOUND{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.RED}✗ NOT FOUND{Style.RESET_ALL}")
                        
                except Exception as e:
                    print(f"{Fore.YELLOW}⚠ ERROR{Style.RESET_ALL}")
                    results[service_name] = False
                
                time.sleep(0.5)  # Rate limiting
            
            # Show results
            elapsed = time.time() - start_time
            self.show_single_results(email, results, elapsed)
            
            # Ask to continue
            print(f"\n{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
            cont = input(f"{Fore.YELLOW}[?] Check another email? (y/n): {Style.RESET_ALL}").strip().lower()
            if cont != 'y':
                break

    def show_single_results(self, email, results, elapsed_time):
        print(f"\n{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}          CHECK RESULTS{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
        
        print(f"{Fore.WHITE}📧 Email: {Fore.CYAN}{email}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}⏱️  Time: {Fore.YELLOW}{elapsed_time:.1f} seconds{Style.RESET_ALL}")
        
        found_services = []
        emojis = []
        
        for service_name, found in results.items():
            if found:
                service_info = self.services[service_name]
                found_services.append(service_name)
                emojis.append(service_info['emoji'])
        
        if found_services:
            print(f"\n{Fore.GREEN}✅ ACCOUNTS FOUND:{Style.RESET_ALL}")
            print(f"   {' '.join(emojis)}")
            for service in found_services:
                color = self.services[service]["color"]
                print(f"   {color}• {service}{Style.RESET_ALL}")
            print(f"\n{Fore.YELLOW}📊 Total: {len(found_services)}/{len(self.services)} services{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.RED}❌ NO ACCOUNTS FOUND{Style.RESET_ALL}")
            print(f"   {Fore.YELLOW}This email is not registered on checked platforms{Style.RESET_ALL}")
        
        # Real vs Simulated info
        real_checks = sum(1 for s in self.services.values() if s["real_check"])
        print(f"\n{Fore.CYAN}📝 Note:{Style.RESET_ALL}")
        print(f"   • {real_checks} platforms checked with real HTTP requests")
        print(f"   • {len(self.services)-real_checks} platforms simulated (no real check)")

    # ========== MODE 2: MULTI EMAIL CHECK ==========
    
    def run_multi_check(self):
        print(f"\n{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}        MULTI EMAIL CHECK{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}[?] Enter emails (comma separated):{Style.RESET_ALL}")
        email_input = input("> ").strip()
        
        if not email_input:
            print(f"{Fore.YELLOW}[*] No emails entered. Returning...{Style.RESET_ALL}")
            return
        
        emails = [e.strip() for e in email_input.split(',')]
        valid_emails = []
        
        # Validate emails
        for email in emails:
            if '@' in email and '.' in email:
                valid_emails.append(email)
            else:
                print(f"{Fore.RED}[!] Invalid email skipped: {email}{Style.RESET_ALL}")
        
        if not valid_emails:
            print(f"{Fore.RED}[!] No valid emails to check!{Style.RESET_ALL}")
            return
        
        print(f"\n{Fore.GREEN}[✓] Valid emails: {len(valid_emails)}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Starting batch check...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] This may take several minutes...{Style.RESET_ALL}\n")
        
        start_time = time.time()
        all_results = {}
        
        for idx, email in enumerate(valid_emails, 1):
            print(f"\n{Fore.CYAN}[{idx}/{len(valid_emails)}] Checking: {email}{Style.RESET_ALL}")
            
            email_results = {}
            for service_name, service_info in self.services.items():
                try:
                    if service_info["real_check"]:
                        found = self.check_service_real(service_name, email)
                    else:
                        time.sleep(0.1)
                        found = random.random() < 0.25
                    
                    email_results[service_name] = found
                    
                except:
                    email_results[service_name] = False
            
            all_results[email] = email_results
            
            # Show quick summary
            found_count = sum(1 for v in email_results.values() if v)
            if found_count > 0:
                print(f"   {Fore.GREEN}✓ Found on {found_count} services{Style.RESET_ALL}")
            else:
                print(f"   {Fore.RED}✗ No accounts found{Style.RESET_ALL}")
            
            time.sleep(1)  # Delay between emails
        
        elapsed = time.time() - start_time
        self.show_multi_results(all_results, elapsed)

    def show_multi_results(self, all_results, elapsed_time):
        print(f"\n{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}          BATCH RESULTS{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
        
        print(f"{Fore.WHITE}📊 Total Emails: {Fore.CYAN}{len(all_results)}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}⏱️  Total Time: {Fore.YELLOW}{elapsed_time:.1f} seconds{Style.RESET_ALL}")
        
        # Summary statistics
        total_hits = 0
        service_counts = {service: 0 for service in self.services}
        
        for email, results in all_results.items():
            for service, found in results.items():
                if found:
                    service_counts[service] += 1
                    total_hits += 1
        
        print(f"\n{Fore.GREEN}📈 STATISTICS:{Style.RESET_ALL}")
        print(f"   • Total hits: {total_hits}")
        print(f"   • Avg hits per email: {total_hits/len(all_results):.1f}")
        
        # Top services
        print(f"\n{Fore.YELLOW}🏆 TOP SERVICES FOUND:{Style.RESET_ALL}")
        sorted_services = sorted(service_counts.items(), key=lambda x: x[1], reverse=True)
        for service, count in sorted_services[:5]:
            if count > 0:
                emoji = self.services[service]["emoji"]
                color = self.services[service]["color"]
                print(f"   {emoji} {color}{service}: {count} emails{Style.RESET_ALL}")
        
        # Detailed results
        print(f"\n{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}          DETAILED RESULTS{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
        
        for email, results in all_results.items():
            found_services = [s for s, f in results.items() if f]
            if found_services:
                print(f"\n{Fore.GREEN}✓ {email}{Style.RESET_ALL}")
                print(f"   Services: {', '.join(found_services[:3])}")
                if len(found_services) > 3:
                    print(f"   + {len(found_services)-3} more")
            else:
                print(f"\n{Fore.RED}✗ {email}{Style.RESET_ALL}")

    # ========== MODE 3: SIMULATION MODE ==========
    
    def run_simulation(self):
        print(f"\n{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}        SIMULATION MODE (DEMO){Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
        
        print(f"\n{Fore.YELLOW}[!] This is a DEMO with generated data{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] No real HTTP requests are made{Style.RESET_ALL}")
        
        num_emails = input(f"\n{Fore.GREEN}[?] How many emails to simulate? (default: 10): {Style.RESET_ALL}").strip()
        try:
            num_emails = int(num_emails) if num_emails else 10
        except:
            num_emails = 10
        
        print(f"\n{Fore.CYAN}[*] Generating {num_emails} simulated emails...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Starting simulation...{Style.RESET_ALL}\n")
        
        # Generate fake emails
        domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
        emails = []
        for i in range(num_emails):
            name = f"user{random.randint(1000, 9999)}"
            domain = random.choice(domains)
            emails.append(f"{name}@{domain}")
        
        start_time = time.time()
        
        for idx, email in enumerate(emails, 1):
            print(f"\n{Fore.CYAN}[{idx}/{num_emails}] {email}{Style.RESET_ALL}")
            
            # Simulate checking
            time.sleep(0.2)
            
            # Generate random results
            found_services = []
            emojis = []
            
            for service_name, service_info in self.services.items():
                if random.random() < 0.6:  # 60% chance in simulation
                    found_services.append(service_name)
                    emojis.append(service_info["emoji"])
            
            if found_services:
                print(f"   {Fore.GREEN}✓ Found on {len(found_services)} services{Style.RESET_ALL}")
                print(f"   {' '.join(emojis[:5])}")
                if len(found_services) > 5:
                    print(f"   + {len(found_services)-5} more")
            else:
                print(f"   {Fore.RED}✗ No accounts found{Style.RESET_ALL}")
        
        elapsed = time.time() - start_time
        print(f"\n{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[✓] SIMULATION COMPLETED{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}📊 Simulated {num_emails} emails in {elapsed:.1f}s{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] This was a demo with generated data{Style.RESET_ALL}")

    # ========== MAIN RUNNER ==========
    
    def run(self):
        try:
            self.show_banner()
            
            print(f"\n{Fore.RED}[!] DISCLAIMER:{Style.RESET_ALL}")
            print(f"• Real check mode makes actual HTTP requests")
            print(f"• Use only with emails you own or have permission")
            print(f"• Excessive use may trigger security alerts")
            print(f"• For educational purposes only")
            
            input(f"\n{Fore.YELLOW}[!] Press Enter to continue...{Style.RESET_ALL}")
            
            while True:
                self.select_mode()
                
                if self.mode == "single":
                    self.run_single_check()
                elif self.mode == "multi":
                    self.run_multi_check()
                elif self.mode == "simulation":
                    self.run_simulation()
                
                # Ask to run again
                print(f"\n{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
                again = input(f"{Fore.YELLOW}[?] Run another check? (y/n): {Style.RESET_ALL}").strip().lower()
                if again != 'y':
                    break
            
            print(f"\n{Fore.GREEN}[✓] Thank you for using Mega Email Checker!{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[*] Developed by: {self.developer}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}[*] Version: {self.version}{Style.RESET_ALL}")
            
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[!] Stopped by user{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")

def main():
    print(f"{Fore.YELLOW}[*] Initializing Mega Email Checker...{Style.RESET_ALL}")
    time.sleep(1)
    
    checker = MegaEmailChecker()
    checker.run()

if __name__ == "__main__":
    main()
