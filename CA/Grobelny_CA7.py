# ! / u s r / b i n / p y t h o n 
 
 i n _ f i l e   =   ' / h o m e / a - m / i b 5 0 1 _ s t u d 1 2 / s h e l l / f s t / b a t c h _ 2 . f s t _ 1 - 2 . t s v ' 
 f s t _ t o t a l   =   0 . 0 
 c o u n t   =   0 
 
 #   C r e a t e   a   d i c t i o n a r y   o f   c h r o m o s o m e s 
 c h r o m   =   { } 
 
 f h   =   o p e n ( i n _ f i l e ,   ' r ' ) 
 n e x t ( f h ) 
 
 #   I t e r a t e   o v e r   e a c h   l i n e   i n   t h e   f i l e 
 f o r   l i n e   i n   f h : 
         #   R e m o v e   n e w   l i n e s 
         l i n e   =   l i n e . s t r i p ( ' \ n ' ) 
         #   W e   c a n   s p l i t   T S V   f i l e s 
         p a r t s   =   l i n e . s p l i t ( ' \ t ' ) 
 
         #   p r i n t   t h e   f s t   v a l u e 
         c o u n t   =   c o u n t   +   1 
         f s t _ t o t a l   =   f l o a t ( p a r t s [ 8 ] )   +   f l o a t ( f s t _ t o t a l ) 
 
         #   s a v e   c h r o m o s o m e s   n u m b e r   w i t h   c o u n t   n u m b e r 
         c h r o m [ c o u n t ]   =   p a r t s [ 4 ] 
 
 #   p r i n t   a v g   f s t 

 p r i n t   " p r i n t i n g   a v g   f s t : " ,   f l o a t ( f s t _ t o t a l )   /   f l o a t ( c o u n t ) 
 
 #   p r i n t   u n i q   c h r o m o s o m e s 
 
 c h r o m _ u n i q   =   l i s t ( ) 
 f o r   i   i n   c h r o m . v a l u e s ( ) : 
         i f   i   i n   c h r o m _ u n i q : 
                 c o n t i n u e 
         e l s e : 
                 c h r o m _ u n i q . a p p e n d ( i ) 
 p r i n t   " h e r e   t h e   l i s t   o f   u n i q   c h r o m o s o m e s : " ,   c h r o m _ u n i q 
 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 #   u n i x   s o l u t i o n s 
 
 #   c a t   ~ / s h e l l / f s t / b a t c h _ 2 . f s t _ 1 - 2 .  t s v   |   s e d   1 d   |   c u t   - f   9   |   a w k   ' { t o t a l _ l i n e s = t o t a l _ l i n e s + $ 1 }   E N D   { p r i n t   t o t a l _ l i n e s / N R } ' 
 #   $   0 . 0 0 1 7 9 0 9 3 
 
 #   c a t   ~ / s h e l l / f s t / b a t c h _ 2 . f s t _ 1 - 2 . t s v   |   s e d   1 d   |   c u t   - f   5   |   s o r t   - h   |   u n i q   |   s o r t   - h 
 
