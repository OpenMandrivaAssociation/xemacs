;;; Linux-Mandrake Configuration for XEmacs
; Chmouel Boudjnah <chmouel@mandrakesoft.com>
; Pixel <pixel@mandrakesoft.com>
; Frederic Lepied <flepied@mandrakesoft.com>
; Warly <warly@mandrakesoft.com>

;; Macros to detect if we are under X.
(defmacro Xlaunch (&rest x) (list 'if (eq window-system 'x)(cons 'progn x)))

; Under X to get the suppr key working.
(Xlaunch (define-key global-map [(delete)] "\C-d"))

;;; XEmacs compatibility
(global-set-key [(control tab)] `other-window)
(global-set-key [(meta g)] `goto-line)
(defun switch-to-other-buffer () (interactive) (switch-to-buffer (other-buffer)))
(global-set-key [(meta control ?l)] `switch-to-other-buffer)
(global-set-key [(meta O) ?H] 'beginning-of-line)
(global-set-key [(meta O) ?F] 'end-of-line)

;;; EuroSign
(global-set-key [EuroSign] (lambda()(interactive)(insert "¤")))

; Don't add lines on the end of lines unless we want.
(setq next-line-add-newlines nil)

; X selection manipulation
;(defun x-own-selection (s) (x-set-selection `PRIMARY s))
;(global-set-key [(shift insert)] '(lambda () (interactive) (insert (x-get-selection))))
;(global-set-key [(control insert)] '(lambda () (interactive) 
;                                     (x-own-selection (buffer-substring (point) (mark)))))

; Shift-arrows a la windows...
(custom-set-variables
 '(pc-select-meta-moves-sexps t)
 '(pc-select-selection-keys-only t)
 '(pc-selection-mode t ))

;; Show parenthesis mode
;(show-paren-mode)

;; By default we starting in text mode.
(setq initial-major-mode (lambda () (text-mode) (turn-on-auto-fill) (font-lock-mode)))

; Don't ask to revert for TAGS
(setq revert-without-query (cons "TAGS" revert-without-query))

;; Use the following for i18n
;(standard-display-european t)
;(set-language-environment "latin-1")

;; Color and Fonts.
(require 'font-lock)
(setq font-lock-mode-maximum-decoration t)
(Xlaunch (set-face-font 'default "-*-Fixed-Medium-R-*-*-*-130-*-*-*-*-iso8859-1"))

;; turn on colorization.
(Xlaunch(if (fboundp 'global-font-lock-mode)(global-font-lock-mode t)))

; Turn on selection and change the default color
(setq transient-mark-mode 't highlight-nonselected-windows 't)

;; Locales variables adapted from Debian.el for Linux-Mandrake.
(setq Info-directory-list
      '("/usr/share/info/xemacs" "/usr/share/info/xemacs/mule" "/usr/share/info" "/usr/local/info"
        "/usr/share/xemacs/packages/info"
        "/usr/share/xemacs/mule-packages/info"
        "/usr/share/xemacs/site-packages/info"))

(setq Info-additional-search-directory-list
      '("/usr/info/" "/usr/info/xemacs"))

(setq news-path "/var/spool/news")

(custom-set-variables ;; '(nnmail-spool-file "/var/spool/mail/$user")
                      '(gnuserv-program 
                          (concat exec-directory "/gnuserv")))

(defun dir-and-all-good-subs (this-directory)
  "Returns list of argument and all subdirectories of argument not
starting with a '.'"
  (if (file-exists-p this-directory)
      (append (list (expand-file-name this-directory))
              (mapcar '(lambda (dir-string)
                         (concat dir-string "/")) 
                      (directory-files 
                       (expand-file-name this-directory) 
                       t "^[^\\.]" nil 1)))
    nil))

(setq load-path
      (let* ((point
              (string-match "[0-9]*\.[0-9]*.*XEmacs.*"
                            emacs-version))
             (xemacs-maj-version
              (substring emacs-version point (+ point 2)))
             (xemacs-version
              (substring emacs-version point (+ point 5))))
        (append
         `(,@(dir-and-all-good-subs "/usr/local/share/xemacs/site-lisp")
             ,@(dir-and-all-good-subs "/usr/share/xemacs/")
             ,@(dir-and-all-good-subs (concat "/usr/share/xemacs-" xemacs-version "/")))
         load-path
         ;;,@(dir-and-all-good-subs
         ;; (concat "/usr/share/xemacs-" xemacs-version "/lisp/"))
         '("/usr/share/xemacs/site-lisp"))))


;; Load package or local system startup files
(let* ((paths '("/etc/emacs/site-start.d"))
         ;; Get a list of all the files in all the specified
         ;; directories that match the pattern.
       (files
       (apply 'append 
              (mapcar 
               (lambda (dir) 
                 (directory-files dir t "^.*\\.el$" nil))
               paths))))
  (mapcar
   (lambda (file)
     (if debug-on-error
        (load-file file)
       (condition-case ()
          (load file nil)
        (error (message "Error while loading %s" file)))))
   files)
  )

;; aspell is defaut

(setq-default ispell-program-name "aspell")
 (setq-default ispell-extra-args '("--reverse"))



;; Local Variables:
;; mode: emacs-lisp
;; End:
